#!/usr/bin/env python
# coding: utf-8

# In[55]:


#########################################################################
#########------- Machine Learning Inmersion ------------#################
#########################################################################
# Capacitador: André Omar Chávez Panduro
# email: andre.chavez@urp.edu.pe
# Introduccion Python - Data Wrangling
# version: 1.0
#########################################################################


# El **data wrangling**, a veces denominada **data munging**, es el proceso de transformar y mapear datos de un dataset *raw* (en bruto) en otro formato con la intención de hacerlo más apropiado y valioso para una variedad de propósitos posteriores, como el análisis. Un **data wrangler** es una persona que realiza estas operaciones de transformación.
# 
# Esto puede incluir munging, visualización de datos, agregación de datos, entrenamiento de un modelo estadístico, así como muchos otros usos potenciales. 

# ![image.png](attachment:image.png)

# In[8]:


import pandas as pd # Pandas es la libreria o el modulo de Python de input/output a la data


# In[11]:


data = pd.read_csv("C:/Users/Andre Chavez/Downloads/Churn-arboles.csv")


# In[3]:


# La dimension del dataset
data.shape # Observaciones, variables


# In[8]:


# Observamos los primeros valores de los datos
#data.head(1)
data.tail()


# ### Crear un subconjunto de datos

# #### Subconjunto de columna o columnas

# In[9]:


data_Genero = data["SEXO"]


# In[10]:


data_Genero.head()


# In[9]:


type(data_Genero)


# In[11]:


subset = data[["EDAD", "CIVIL", "INGRESO"]]


# In[12]:


subset.head()


# In[12]:


data.head(1)


# In[1]:


# Ejercicio N°01
# Crear un dataframe con las columnas SEXO, INGRESO Y la variable Target


# In[14]:



#subset2.head(3)


# In[11]:


type(subset)


# In[15]:


# Siempre es muy usado generar una lista de nombres de columnas y después generar el subset de datos
columnas_input = ["EDAD","AUTO"]
# Del dataset elegimos las columnas anteriormente seleccionadas
subset = data[columnas_input]
# Mostramos lo deseado
subset.head()


# In[16]:


data.head(1)


# In[2]:


# Ejercicio N°02
# Generar una lista de variables con las variables Estado Civil, Ingreso y auto.


# In[20]:


# Podemos generar otra lista de columnas que no deseemos y por complemento retirarlas del set de datos
columnas_no_input = ["ID", "EDAD"]
columnas_no_input


# In[18]:


# Genero la lista total de variables
columnas_totales = data.columns.values.tolist()
columnas_totales


# In[21]:


# Me quedo con las columnas necesarias
columnas_complemento = [x for x in columnas_totales if x not in columnas_no_input]
columnas_complemento


# In[22]:


subset2 = data[columnas_complemento]
subset2.head()


# In[21]:


# Ejercicio N°03
# Generar una lista con columnas no deseadas como CIVIL, AUTO, HIJOS y CHURN, y de las columnas totales suprimirlas


# #### Subconjunto de filas

# In[24]:


data[:10]


# In[23]:


data[0:15]


# In[24]:


data[:15] # CORRECCIÓN: es lo mismo que data[0:8]


# In[27]:


data[0:4]


# #### Subconjuntos de filas con condiciones booleanas

# In[25]:


## Clientes con INGRESO > 30000
data1 = data[data["INGRESO"]>30000]
data1.head(3)


# In[26]:


data.CHURN.value_counts()


# In[27]:


## Clientes Fugados (CHURN = "Fuga")
data2 = data[data["CHURN"]=="Fuga"]
data2.head(4)


# In[28]:


## AND -> &
data3 = data[(data["INGRESO"]>30000) & (data["CHURN"]=="No Fuga")]
data3.shape


# In[29]:


## OR -> |
data4 = data[(data["SEXO"]=="Femenino") | (data["CHURN"]=="Fuga")]
data4.head(6)


# In[38]:


# Ejercicio N°04
# Generar un subset de clientes con ingresos mayores a 1000 soles, No Fugados y con edades mayores a 28 años.


# In[39]:


## EDAD, AUTO y CHURN de los primeros 20 individuos
subset_primeros_50 = data[["EDAD", "AUTO", "CHURN"]][:50]
subset_primeros_50.head()


# In[40]:


subset[:10]


# #### Filtrado con ix -> loc e iloc

# In[30]:


data.ix[1:10, 3:6] ## Primeras 10 filas, columnas de la 3 a la 6


# In[32]:


data.iloc[0:10 , 2:6] # data[filas,columnas]


# In[31]:


data.iloc[:,3:6] ##Todas las filas para las columnas entre la 3 y la 6
data.iloc[1:10,:] ##Todas las columnas para las filas de la 1 a la 10


# In[37]:


# Generamos un subset a nivel de filas y columnas
#data.iloc[1:10,[2,5,7]]
data.iloc[0:20,[1,5]]


# In[35]:


# Puedo hacer el subset de acuerdo a lo que necesite
data.iloc[[1,5,8,36], [2,5,7]]


# In[36]:


data.iloc[[1,5,8,36], [2, 3, 4]]


# #### Insertar nuevas filas en el dataframe

# In[38]:


data["Ingreso/Hijo"] = data["INGRESO"]/(data["HIJOS"]+1)


# In[39]:


data.head()


# In[48]:


data.head(5)


# In[49]:


# Ejercicio N°05
# Generar la variable INGRESO/EDAD o Numero de hijos **2
import numpy as np
np.power(variable,2)


# In[52]:


data.shape


# In[53]:


data.head()


# ### Generación aleatoria de números

# In[59]:


import numpy as np


# In[72]:


##Generar un número aleatorio entero entre 1 y 100
np.random.randint(1,100)


# In[76]:


##La forma más clásica de generar un número aleatorio es entre 0 y 1 (con decimales)
np.random.random()


# In[54]:


## FIN

