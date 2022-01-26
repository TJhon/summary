#!/usr/bin/env python
# coding: utf-8

# # Script para generar la solución del Primer Benchmark de la Competencia
# 
# ## Si no presentaste aún tu primera solución, tenes la oportunidad de hacerlo en pocos Clicks!
# 
# **Hola! **  
#   
# Este Script es un Ejemplo de Procesamiento de los Datos, Modelado y Generación de una Solución.
# 
# Agregamos una pequeña explicación de lo que se hace en cada paso para ayudar a los que están comenzando ahora
# 

# ### Importamos las librerías que vamos a utilizar

# In[1]:


import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold
import re


# ### Lectura de las Bases
# 
# Observamos los datos que tenemos disponibles en https://www.kaggle.com/c/interbank20/data
# 
# Vamos a trabajar ahora con todas las bases disponibles

# In[4]:


rcc_train = pd.read_csv("Data/rcc_train.csv")
se_train = pd.read_csv("Data/se_train.csv", index_col="key_value")
censo_train = pd.read_csv("Data/censo_train.csv", index_col="key_value")
y_train = pd.read_csv("Data/y_train.csv", index_col="key_value").target

rcc_test= pd.read_csv("Data/rcc_test.csv")
se_test= pd.read_csv("Data/se_test.csv", index_col="key_value")
censo_test= pd.read_csv("Data/censo_test.csv", index_col="key_value")


# ### Vamos a trabajar ahora con la base de **RCC**:
# * Discretizamos los días de atraso para poder manipularla mejor
# * Hacemos tablas cruzadas sobre key_value y cada variable de interés, utilizando distintas funciones de agregación sobre el saldo del producto

# In[5]:


bins = [-1, 0, 10, 20, 30, 60, 90, 180, 360, 720, float("inf")]
rcc_train["condicion"] = pd.cut(rcc_train.condicion, bins)
rcc_test["condicion"] = pd.cut(rcc_test.condicion, bins)


# In[6]:


def makeCt(df, c, aggfunc=sum):
    try:
        ct = pd.crosstab(df.key_value, df[c].fillna("N/A"), values=df.saldo, aggfunc=aggfunc)
    except:
        ct = pd.crosstab(df.key_value, df[c], values=df.saldo, aggfunc=aggfunc)
    ct.columns = [f"{c}_{aggfunc.__name__}_{v}" for v in ct.columns]
    return ct


# In[7]:


train = []
test = []
aggfuncs = [len, sum, min, max]
for c in rcc_train.drop(["codmes", "key_value", "saldo"], axis=1):
    print("haciendo", c)
    train.extend([makeCt(rcc_train, c, aggfunc) for aggfunc in aggfuncs])
    test.extend([makeCt(rcc_test, c, aggfunc) for aggfunc in aggfuncs])


# In[17]:


import gc

del rcc_train, rcc_test
gc


# In[ ]:


gc 


# In[9]:


train = pd.concat(train, axis=1)
test = pd.concat(test, axis=1)


# ### Incorporamos la Información adicional existente en las tablas socio económicas y del censo. Es un simple join porque ambas tienen key_value únicos
# #### Por el momento no incorporamos la información tributaria porque requiere un tratamiento más complejo que queda para futuras revisiones

# In[10]:


train = train.join(censo_train).join(se_train)
test = test.join(censo_test).join(se_test)

del censo_train, se_train, censo_test, se_test
gc.collect()


# ### Por la naturaleza de las variables creadas, nos aseguramos que solo se utilicen variables existentes en ambos conjuntos de datos (train y test)

# In[11]:


keep_cols = list(set(train.columns).intersection(set(test.columns)))
train = train[keep_cols]
test = test[keep_cols]
len(set(train.columns) - set(test.columns)) , len(set(test.columns) - set(train.columns))


# In[12]:


test = test.rename(columns = lambda x:re.sub('[^A-Za-z0-9_-]+', '', x))
train = train.rename(columns = lambda x:re.sub('[^A-Za-z0-9_-]+', '', x))


# In[13]:


folds = [train.index[t] for t, v in KFold(5).split(train)]


# ### Entrenamiento del Modelo
# 
# Para entrenar nuestro modelo vamos a usar LightGBM. A diferencia del notebook anterior, esta vez vamos a agregar la optimización de hyper-parámetro. Se usan sólo dos con algunos pocos posibles valores, a modo de ejemplo para que los participantes lo puedan ir mejorando. 

# In[14]:


from sklearn.model_selection import ParameterGrid

params = ParameterGrid({"min_child_samples": [150, 250, 500, 1000], "boosting_type": ["gbdt", "goss"]})


# In[15]:


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
    


# ### Guardado de las predicciones modelo para hacer la presentación
# 
# Finalmente creamos el archivo CSV que podemos subir como nuestra Solución a la competencia

# In[16]:


best_probs.name = "target"
best_probs.to_csv("benchmark2.csv")


# In[19]:


best_probs

