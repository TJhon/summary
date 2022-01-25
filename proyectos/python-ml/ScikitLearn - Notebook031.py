#!/usr/bin/env python
# coding: utf-8

# In[56]:


#########################################################################
#########------- Machine Learning Inmersion ------------#################
#########################################################################
# Capacitador: André Omar Chávez Panduro
# email: andre.chavez@urp.edu.pe
# Introduccion Python - DesarrolloAlgoritmosMachineLearning
# version: 1.0
#########################################################################


# ![image.png](attachment:image.png)

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np # Trabajar con arreglos ( Vectores y matrices)
import pandas as pd # Lectura de datos (Input/Output)
import matplotlib.pyplot as plt # Graficos en Python
np.random.seed(42)


# En primer lugar vamos a probar con un ejemplo muy sencillo: ajustar una recta a unos datos. Esto difícilmente se puede llamar _machine learning_, pero nos servirá para ver cómo es la forma de trabajar con `scikit-learn`, cómo se entrenan los modelos y cómo se calculan las predicciones.

# In[2]:


# Lectura de datos
data = pd.read_csv("C:/Users/Andre Chavez/Desktop/Data/Churn-arboles.csv")


# In[5]:


# Ver los primeros
data.head()


# In[3]:


# Cambiamos los datos string a numeros para que los algoritmos puedan trabajar
# *


# In[7]:


from sklearn.preprocessing import LabelEncoder

for c in columnas_categoricas:
    print(str(c))
    le = LabelEncoder()
    le.fit(data[str(c)])
    data[str(c)]=le.transform(data[str(c)]) 


# In[8]:


# Observar el encoding
data.head(10)


# In[22]:


#data.dtypes


# El proceso para usar `scikit-learn` es el siguiente:
# 
# 1. Separar los datos en matriz de características `features` y variable a predecir `y`
# 2. Seleccionar el modelo
# 3. Elegir los hiperparámetros
# 4. Ajustar o entrenar el modelo (`model.fit`)
# 5. Predecir con datos nuevos (`model.predict`)

# In[9]:


# Paso1: Llamamos un modelo analítco
# Llamamos a la libreria de modelos
from sklearn.linear_model import LogisticRegression


# In[10]:


# Paso2: Definimos el modelo
lr = LogisticRegression() # Utiliza los parámetros por defecto


# In[11]:


# Generamos el frame de drivers o features.
# X - y
drivers=["EDAD","SEXO","CIVIL","HIJOS","INGRESO","AUTO"]
X = data[drivers]


# In[12]:


X.head(3)


# In[13]:


# Generamos el frame del target o variable objetivo
y=data["CHURN"]


# In[14]:


# Paso 03:  Particion muestral
from sklearn.model_selection import train_test_split


# In[15]:


# X_train, X_test, Y_train, Y_test =
X_train, X_test, y_train, y_test = train_test_split(X, # Drivers o covariables
                                                    y, # Target
                                                    test_size=0.30)


# In[16]:


# Paso04: Ajusto un modelo predictivo
lr.fit(X_train, y_train) # Ajuste o entrenamiento


# In[17]:


# Paso05: Predecimos con el algoritmo entrenado
y_pred_train = lr.predict(X_train)
y_pred_test =  lr.predict(X_test)


# Para calcular el error, en el módulo `sklearn.metrics` tenemos varias funciones útiles:

# In[18]:


# Paso06: Validamos el mdodelo predictivo
from sklearn import metrics


# In[19]:


precision_global_train = metrics.accuracy_score(y_true=y_train, y_pred=y_pred_train)
precision_global_test =  metrics.accuracy_score(y_true=y_test,   y_pred=y_pred_test)


# In[20]:


precision_global_train


# In[21]:


precision_global_test


# Y ahora predecimos con datos nuevos:

# In[22]:


# Paso6: Implementamos un modelo predictivo
data_new = pd.read_csv("C:/Users/Andre Chavez/Desktop/Data/Churn-arboles-nuevos.csv")


# In[23]:


data_new.head(2)


# In[24]:


# Le hacemos label encoding tambien
columnas_categoricas = ["SEXO","CIVIL","AUTO"]
for c in columnas_categoricas:
    print(str(c))
    le = LabelEncoder()
    le.fit(data_new[str(c)])
    data_new[str(c)]=le.transform(data_new[str(c)]) 


# In[28]:


# data_new.head(1)


# In[25]:


# Le retiramos el ID o identificador unico
data_new02 = data_new.drop("ID",axis=1)


# In[26]:


# Paso07: Con el modelo entrenado, hago la prediccion para nuevos individuos
y_campanas = lr.predict(data_new02)


# In[27]:


y_campanas


# In[28]:


# Informacion que tenemos que mandar a campanas
import pandas as pd
dataCampanas = pd.DataFrame(np.hstack((data_new['ID'].values.reshape(-1,1), y_campanas.reshape(-1,1))))
dataCampanas.to_csv("DataCampanas.csv")


# ¡Y ya está! Lo básico de `scikit-learn` está aquí. Lo próximo será usar diferentes tipos de modelos y examinar con rigor su rendimiento para poder seleccionar el que mejor funcione para nuestros datos.

# In[77]:


# FIN!!

