import pandas as pd

full = pd.read_csv("https://raw.githubusercontent.com/TJhon/maratona/main/d2/clean_data.csv")
answ = pd.read_csv("https://raw.githubusercontent.com/maratonadev/desafio-2-2021/main/assets/answers.csv")
#full.info()
#answ.info()

features = ['ILLUM', 'HUMID', 'CO2', 'SOUND', 'TEMP']
target = ['RYTHM']

x = full[features]
y = full[target]

from sklearn.linear_model import ElasticNet, Lasso,  BayesianRidge, LassoLarsIC
from sklearn.ensemble import RandomForestRegressor,  GradientBoostingRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import r2_score as r2
from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
import xgboost as xgb
import lightgbm as lgb

from sklearn.linear_model import Ridge


from sklearn.preprocessing import StandardScaler

#sclr = StandardScaler()
#x_train = sclr.fit_transform(x_train)
#x_test = sclr.transform(x_test)
#answer_pred = sclr.fit_transform(answer_pred)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.45, random_state = 23)

rs = 1
lm = LinearRegression()
lasso = make_pipeline(RobustScaler(), Lasso(alpha = 0.0005, random_state = rs))
enet = make_pipeline(RobustScaler(), ElasticNet(alpha = 0.0005, l1_ratio = .4, random_state = rs))
#krr = KernelRidge(alpha = 0.6, kernel = "polinomial", degree = 2, coef0 = 2.5)
gbost = GradientBoostingRegressor(
    n_estimators = 3000, learning_rate = 0.05
    , max_depth = 4, max_features = "sqrt"
    , min_samples_leaf = 15, min_samples_split = 10
    , loss = 'huber', random_state = rs
)
lgb_md = lgb.LGBMRegressor(
    objetive = "regression", num_leaves = 5, learning_rate = 0.05,
    n_estimators = 500, max_bin = 55, bagging_fraction = 0.8,
    bagging_freq = 5, feature_fraction = 0.2319
    , feature_fraction_seed = 9, bagging_seed = 9
    , min_data_in_leaf = 6, min_sum_hessian_in_leaf = 11
)

model_xgb = xgb.XGBRegressor()
ridge = Ridge(
    alpha=0.5848729102193255,
    copy_X=False,
    max_iter=46,
    random_state=33,
    solver="sag",
    tol=0.004677115268539831,
)





def r_2(model):
  model.fit(x_train, y_train)
  y_pred = model.predict(x_test)
  r_2 = r2(y_test, y_pred)
  print(r_2 )


r_2(lm)
#r_2(lasso)
#r_2(enet)
##r_2(krr)
##r_2(gbost)
#r_2(lgb_md)
#r_2(model_xgb)
#r_2(ridge)



answ[target] = lm.fit(x_train, y_train).predict(answ[features])

answ.to_csv("d2.csv", index = False)
