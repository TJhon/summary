
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold
import re





rcc_train = pd.read_csv("Data/rcc_train.csv")
se_train = pd.read_csv("Data/se_train.csv", index_col="key_value")
censo_train = pd.read_csv("Data/censo_train.csv", index_col="key_value")
y_train = pd.read_csv("Data/y_train.csv", index_col="key_value").target

rcc_test= pd.read_csv("Data/rcc_test.csv")
se_test= pd.read_csv("Data/se_test.csv", index_col="key_value")
censo_test= pd.read_csv("Data/censo_test.csv", index_col="key_value")




bins = [-1, 0, 10, 20, 30, 60, 90, 180, 360, 720, float("inf")]
rcc_train["condicion"] = pd.cut(rcc_train.condicion, bins)
rcc_test["condicion"] = pd.cut(rcc_test.condicion, bins)




def makeCt(df, c, aggfunc=sum):
    try:
        ct = pd.crosstab(df.key_value, df[c].fillna("N/A"), values=df.saldo, aggfunc=aggfunc)
    except:
        ct = pd.crosstab(df.key_value, df[c], values=df.saldo, aggfunc=aggfunc)
    ct.columns = [f"{c}_{aggfunc.__name__}_{v}" for v in ct.columns]
    return ct




train = []
test = []
aggfuncs = [len, sum, min, max]
for c in rcc_train.drop(["codmes", "key_value", "saldo"], axis=1):
    print("haciendo", c)
    train.extend([makeCt(rcc_train, c, aggfunc) for aggfunc in aggfuncs])
    test.extend([makeCt(rcc_test, c, aggfunc) for aggfunc in aggfuncs])




import gc

del rcc_train, rcc_test
gc


gc 



train = pd.concat(train, axis=1)
test = pd.concat(test, axis=1)



train = train.join(censo_train).join(se_train)
test = test.join(censo_test).join(se_test)

del censo_train, se_train, censo_test, se_test
gc.collect()




keep_cols = list(set(train.columns).intersection(set(test.columns)))
train = train[keep_cols]
test = test[keep_cols]
len(set(train.columns) - set(test.columns)) , len(set(test.columns) - set(train.columns))



test = test.rename(columns = lambda x:re.sub('[^A-Za-z0-9_-]+', '', x))
train = train.rename(columns = lambda x:re.sub('[^A-Za-z0-9_-]+', '', x))


folds = [train.index[t] for t, v in KFold(5).split(train)]




from sklearn.model_selection import ParameterGrid

params = ParameterGrid({"min_child_samples": [150, 250, 500, 1000], "boosting_type": ["gbdt", "goss"]})


best_score = 0
best_probs = []
for param in params:
    test_probs = []
    train_probs = []
    p  = "///".join([f"{k}={v}" for k, v in param.items()])
    print("*"*10, p, "*"*10)
    for i, idx in enumerate(folds):
        Xt = train.loc[idx]
        yt = y_train.loc[Xt.index]

        Xv = train.drop(Xt.index)
        yv = y_train.loc[Xv.index]

        learner = LGBMClassifier(n_estimators=1000, **param)
        learner.fit(Xt, yt,  early_stopping_rounds=10, eval_metric="auc",
                    eval_set=[(Xt, yt), (Xv, yv)], verbose=False)
        test_probs.append(pd.Series(learner.predict_proba(test)[:, -1], index=test.index, name="fold_" + str(i)))
        train_probs.append(pd.Series(learner.predict_proba(Xv)[:, -1], index=Xv.index, name="probs"))

    test_probs = pd.concat(test_probs, axis=1).mean(axis=1)
    train_probs = pd.concat(train_probs)
    score = roc_auc_score(y_train, train_probs.loc[y_train.index])
    print(f"roc auc estimado para {p}: {score}")
    if score > best_score:
        print("*"*10, f"{p} es el nuevo mejor modelo", "*"*10)
        best_score = score
        best_probs = test_probs
    





best_probs.name = "target"
best_probs.to_csv("benchmark2.csv")




best_probs

