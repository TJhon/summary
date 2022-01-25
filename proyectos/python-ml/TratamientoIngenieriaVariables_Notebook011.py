#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#########################################################################
#########------- Machine Learning Inmersion ------------#################
#########################################################################
# Capacitador: André Omar Chávez Panduro
# email: andre.chavez@urp.edu.pe
# Tema:  Tratamiento e Ingeniería Variables
# version: 1.0
#########################################################################


# ### **Tratamiento e Ingeniería Variables**
# 
# La ingeniería de características es el proceso de usar el conocimiento del dominio para extraer características de datos sin procesar a través de técnicas de minería de datos. Estas características se pueden usar para mejorar el rendimiento de los algoritmos de aprendizaje automático.

# In[ ]:


# Conexion a Google Colaborative
from google.colab import drive
drive.mount('/gdrive')


# In[ ]:


## Podemos hacer el balanceo de manera artesanal , para entender las lógicas.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### **1. Carga de base de datos**
# 
# Desarrollar el mejor modelo de propensión que prediga si se logrará la venta de un préstamo digital.

# In[ ]:


df = pd.read_csv('',sep=";")


# In[ ]:





# In[ ]:


# Vemos la distribucion del target!


# In[ ]:


# Visualizando la variable target
sns.factorplot('ventaPrestDig',data=df,kind="count")


# In[ ]:


# Visualizamos los registros del dataset
df.head(3)


# In[ ]:


### **2. Tratamientos o Recodificacion de variables**


# In[ ]:


ColumnsCategoricas = ['estadoCliente','rngEdad','genero','rngSueldo','procedencia','operDigital','tenTarjeta']
ColumnsNumericas =   ['trxDigitalUm','promTrxDig3Um','recCamp','frecCamp','promConsBanco3Um','promSaldoBanco3Um','promSaldoTc3Um','promSaldoPrest3Um','sowTcUm','sowPrestUm']


# In[ ]:


# Antes de hacer cualquier trabajo con los datos, vemos los valores nulos!


# In[ ]:


# Creamos 2 dataset de variables categoricas!
df_categoricas_01 = df[ColumnsCategoricas]
df_categoricas_02 = df[ColumnsCategoricas]


# In[ ]:


# Tratamiento de Variables Categoricas
# LabelEncoder
from sklearn.preprocessing import LabelEncoder

for c in df_categoricas_01:
    print(str(c))
    le = LabelEncoder()
    le.fit(df_categoricas_01[str(c)])
    df_categoricas_01[str(c)]=le.transform(df_categoricas_01[str(c)]) 


# In[ ]:


# Tratamiento de Variables Categoricas
# Preprocesamiento con OneHotEncoder
df_categoricas_03 = pd.get_dummies(df_categoricas_02)


# In[ ]:


# Al final hasta tenemos 2 set de datos o dataset's para poder trabajar!


# In[ ]:


# Concatenamos la informacion para seguir con el analisis!
df2 = 


# In[ ]:


# Hacemos un resumen rapido de las variables numericas
# Es muy importante analizar las variables cuantitativas :


# In[ ]:


# Ayuda visual
for x in ColumnsNumericas:
  Q03 = int(df2[x].quantile(0.75))+100
  plt.title(df2[x].name)
  plt.hist(df2[x], bins= 100 ,range=(0,Q03))
  plt.show()


# ### **3. Ingeniería de variables o Feature Enginnering**

# In[ ]:


# Vista de las variables!


# In[ ]:


# Ingenieria de Variables por Criterio Experto o Decision de Negocio!
df2['promConsSaldoBanco3Um']        =  df2['promConsBanco3Um'] / (df2['promSaldoBanco3Um'] +1)
# Debemos pensar algunas más!


# In[ ]:


# Ingenieria de Variables por Transformaciones no Lineales!
df2['log_promTrxDig3Um']            =  np.log1p(df2['promTrxDig3Um']+1)
# Debemos pensar algunas más!


# In[ ]:


# Vista de las variables!


# In[ ]:


#df2.dtypes


# In[ ]:


# Ingenieria de Variables con Features polinómicos!
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2,interaction_only=False,include_bias= False) # Definimos el grado del polinomio
to_cross = ['promTrxDig3Um', 'promConsBanco3Um', 'promSaldoBanco3Um']          # Definimos las variables con las que queremos jugar!

crossed_feats = poly.fit_transform(df2[to_cross].values)                       # Aplicamos la transformacion polinomica.


# In[ ]:


# Guardamos los nuevos features en un dataframe
crossed_feats = pd.DataFrame(crossed_feats) # Revision de las nuevas variables que crea!


# In[ ]:


# Entendemos lo necesario a extraer!
# Logica: 1^2,1*2,1*3,2^2,2*3,3^2
crossed_feats = pd.DataFrame(crossed_feats.iloc[:,3:9].to_numpy(),columns=['promTrxDig3Um_2','promTrxDig3Um_promConsBanco3Um','promTrxDig3Um_promSaldoBanco3Um','promConsBanco3Um_2','promConsBanco3Um_promSaldoBanco3Um','promSaldoBanco3Um_2'])


# In[ ]:


# Concatenamos la informacion!


# ### **4. Selección de variables o Feature Selection**

# In[ ]:


# Selección por WOESS!


# In[ ]:


final_iv, IV = data_vars(df3,df3.ventaPrestDig)


# In[ ]:


# Ordenamos el ordenamiento!
IV.sort_values('IV',ascending=False)


# In[ ]:





# In[ ]:


# Podemos para ser ordenados, separar las covariables del target!
x= df3.drop('ventaPrestDig',axis=1)
y= df3.ventaPrestDig


# In[ ]:


# Seleccion por Random Forest
from sklearn.ensemble import RandomForestClassifier # Paso01: Instancio el algoritmo
forest = RandomForestClassifier()                   # Paso02: Configuro el algoritmo
forest.fit(x,y)                                     # Paso03: Ajuste el algoritmo
importances = forest.feature_importances_           # Paso04: Variables importantes


# In[ ]:


# Seleccion por Random Forest
TablaImportancia = pd.concat([pd.DataFrame({'Driver':list(x.columns)}),
                              pd.DataFrame({'Importancia':list(forest.feature_importances_)})], axis = 1)
ImportanciaVariables = TablaImportancia[['Driver','Importancia']].sort_values('Importancia', ascending = False).reset_index(drop = True)
#ImportanciaVariables


# ### **5. Modelamiento de información**

# In[ ]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


# In[ ]:


# Vamos a generar nuestro primer algoritmo predictivo o de machine learning!


# In[ ]:


#Separación de predictoras y predicha
X = df3.drop('ventaPrestDig',axis=1)
y = df3.ventaPrestDig


# In[ ]:


#Creación de muestras de train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=22)


# In[ ]:


# Instanciamos el algoritmo de clasificacion!
tree = DecisionTreeClassifier()


# In[ ]:


# Entrenamos!
tree_model = tree.fit(X_train,y_train) # ajustando el modelo a mis datos


# In[ ]:


# Predecimos!
Y_pred = tree_model.predict(X_test) # realizando la predicción


# In[ ]:


#Cálculo del accuracy
accuracy_score(y_test,Y_pred)


# In[ ]:


#Matriz de confusión
conf_mat = confusion_matrix(y_test,Y_pred)
conf_mat


# In[ ]:


# Visualizando la matriz de confusión
labels = ['Class 0', 'Class 1']
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(conf_mat, cmap=plt.cm.Blues)
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('Expected')
plt.show()


# In[ ]:





# In[ ]:


# Visualizando el arbol!
#utils.draw_tree(m, x)


# ### **6. Balanceo de Muestras**

# ![image.png](data:image/png;base64,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xGWKJvnNN9+4ZZdd1p100kmOY9ILL7zg884+++yoXt6D4cOHt4yEP/XUU65Pnz7usccec88++2yHKQ8cODAi4bvvvru7/PLLO9RpmwyRcJHwthHGNplIyMbl52Mucf/6lx46ahNR0jSEQJdFIGQ9WURP+PHHH++22GKLDvJ4++23uyFDhpTkQ9K/+OKLkrz4yaeffho/LXv8+eefly3L2kfaXB555BG30korle178cUXdx9++KEvh4SbJ/yTTz4p26ZSWdlGjSgQCRcJb4QcdaU+QjYu6/7yXHf00Ue7r776qitdEq1FCAiBNkMgZD1ZRBK+4oorumuvvbaqFO2yyy4OT/Laa6/tNt54Yzd16lTfBq8zZVtuuaXPX3TRRd2ECROi/pZeemn30Ucf+fMXX3zRLb/88m6NNdZwq622mjv88MOjeoSHrL766m799dd3AwYMcLfddltUljxIm8sdd9zh1ltvPTfvvPO6ddddN/LqW9utt97a9erVy4eqPPnkkw4Sjqd/ySWXdIMGDXL9+/d3TzzxhFV348eP92E5G2ywgWMNN954Y1TWkgORcJHwlgiaBmkZAhdccIHjoyQEhIAQaBYCIuHNQrY5/f7kJz9xzz//fMXOR40a5Q466KCozmmnnea23357fw4J79atm7v//vv9+VtvveUWXnhh99577/lzSLGRcMjsDTfcEPWzzTbbuEsuucQRk06ZpbvuuquDF97KKs3loYcequoJt5hwSDgEe+bMmb7rU0891e24447++Omnn3YLLbRQtIbXX3/dk/uWPrQqEi4SbkKv7x8QCNm48GAmXnC84ffdd58uqRAQAkKgKQiErCeL6AmfZ5553N///veKskAYB0TUEruoQLxJkHC84/G01VZbRd5wI+EQfYj25MmTo89f/vIXt9lmm3mv+myzzebOOuss98orr8S76nBcaS4PPPBAWfJORz179iyJCR83blzUPz8i8KSTRo8e7X79619H82TOO+20k7viiiui+k0/EAkXCW+6kAU2QMjGxXZHIS583333VXx4YLKn6QqBUBAIWU8WkYQTFnL99denihchHiS8wtOmTSupw04qxEtDwtlZJZ5Gjhzp8CyTjITfc8897qc//aknycSa24fwE9Ldd9/t8Izzo2C55ZYre9e20lxqJeHxBzNpayR8zz339F5ym6N9jx071s+1FX8+fPrmcPcIZ39z7ROeWUy0RWFGqEI2LkbCWSqecMWHZ7zoqiYEhEBNCISsJ4tIwk888UQ3dOjQDtcY0kwMNYk47zfeeCOqk/SEEyMeT2wRaF5jI+HPPPOMW2aZZeLV3Pvvvx896Pnyyy9HZTwUiqfdQkeigipzqUbC8aJbn8ndUeIkHC84Merx9M9//tN9//338aymHT/33HPu8lNHiYQf+edgvOH1CINIeEb0QjYucRLOchUfnvGiq5oQEAI1IRCyniwiCf/yyy8d5JQ4byOZEOalllrK/e53v/PX/tBDD3V8LJ1xxhkRcbeYcOKoSa+++qpbbLHFojhwI+GULbLIIu66666zbtwee+zhwz4Yr1+/fm769Om+jH3FZ599dvf1119Hde2g0lyqkXAe+CRmnVSJhD/88MOud+/ebtKkSb4u4Sg9evRwjz/+uE2jad/crQZfp3CUYAi43pjZtH+H0o5DNi5JEq748NJrqzMhIAQag0DIerKIJJyrjueVsBA834SMEPJxwgknlAgED2KuvPLKvh7hGbbVHyR88ODBbqONNvIf2saJNuTaHsz861//6ncjIYZ8zTXXdNtuu200BndnV1hhBbfJJpv4HVQqbSJQbi5479lhpVwirnuOOeZwt956awcSfu+99/oQFGvLzingwXyIZbcfJFbejG8j4H4XM5FwkfBmCFnIfYZsXJIknOug+PCQpVFzFwLtiUDIerKoJNwkiW0HzftrefFv9vdO7psNCWdLQNIHH3wQr172GFKOBz4tZe0jbS5p/SXzvv3222RWxfOs86nYSYZCiDcecE/AqS8SLhKeQW4KVSVk45JGwrl4ig8vlAhrsUKg6QiErCeLTsLzCEechOdprzbOE28IOI6xKImEi4RHwqADj0DIxqUcCWdhig+XgAsBIdAoBELWkyLhtUsBjhxiu5XyI8AuLcTSlySRcJHwEoHQiQvZuFQi4YoPl3ALASHQKARC1pMi4Y2SAvWTFQEIOHcTOiSRcJHwDkJR8IyQjUslEs5lVXx4wYVbyxcCDUIgZD0pEt4gIVA3mRDgLgKf1CQSLhKeKhgFzgzZuFQj4VxWxYcXWLi1dCHQIARC1pMi4Q0SAnVTFQG83/GXBXVoIBIuEt5BKAqeEbJxyULCubyKDy+4kGv5QqBOBELWkyLhdV58Nc+EAPHfFQl4pl66XiX22w71U8/V0Mt6MqIXsnHJSsIVH55RGFRNCAiBVARC1pMi4amX1GeOGDHC8RKdRiZersMr4i09++yzdlj3N33/8pe/rLufRndQshd4pc7lCQ+KkFe6lNXKRMKrIfR/5SEbl6wknKUqPjyjQKiaEBACHRAIWU+KhHe4nFHG8OHDG07CH3roIbfbbrv5MXhL5XrrrReNV+/BI4884ngpUDslXnBUshd4pcmJhIuEV5KPIpaFbFxqIeFcW8WHF1HCtWYhUD8CIevJopLw77777j8viXHOzZw5s+S8klR88cUXqcWffvppaj6Z06ZN61BGjHQ9JJyX8MRfAFSOhCdfNhSfSLk5V2oTb1/p2F7GY28arVTXl4mEi4RXFZKCVQjZuNRKwrm0ig8vmIBruUKgAQiErCeLRsKXX355d9ppp7mVVlrJLbzwwm7UqFFu7Nix/vX0ffr0cYcddlgkEby63V4/Tzte484r4hdZZBG36aabRvWefPJJt9RSS/nX0q+44oru2GOPjcr22msvd/XVV7t5553Xrbbaag5PON7qKVOmeAJOuzXWWMONGzfOrb/++lE7DjbffHM3YcKEkjw74XX0tKMv6pGSJPzII4/0Y0L0l1hiCXfEEUdYc3fMMcf4tTDmgAED3G233ebL7rzzTjdw4EA/FzA66qijoja1HnR4GU+1DkTCRcKryUjRykM2LnlIuOLDiybhWq8QqB+BkPVk0Uh4r1693JgxY/xF5/XsPXr08KScjHfffdfNP//87vvvv/flEGcj4bPOOmtUj8I111zTXXPNNb5e37593S233OKPabvWWmu5q666yp/vu+++bsMNN3R4nCHJcaIMeTdPOO3mmGOOaDw85/PMM4/vI/mHuO+DDjooyub4uOOOK+n7nnvucSussEJU59///rebffbZveecdfIDw9Jdd93lhgwZ4k8h3hanPmPGDN/H22+/bVUzf/MQ5nPPPZe5vq8oEi4SXpvEdP3aIRuXPCScK6r48K4v11qhEGgkAiHryaKR8Pnmm8+9+eab0eWHdL/33nvROaT8888/9+dxEg6BhbRb2n///d3555/vCWuc7FIOOd9mm2181ZEjR7qTTz7ZmpUQ5QcffDAi4VTggc3f//73vi4e8P322y9qFz/o37+/e/nll6Ms1kNYSpzgU/jZZ5/5OoStQPhnm20274GfOnWqPz7r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r3/t848++mj3i1/8wi244IKRJ/yaa65xCyywgC8fMmSIO/bYY93CCy8c9d27d2+32Wab+fP777/fzTPPPO6uu+6KPPFLLrmk++tf/xrVJ0SGHwh8fvzjH0c/FKqR8Ouuu8717dvXt1t//fVdkoSfdNJJUb/0zR0A0rhx49xcc83ly3r16uXuuecen19uHu+9955bd911o77AAgwsXXLJJX6NjMHa//CHP/iicuNYO30LASEgBNoFAdkI2Yh2kUXNQwi0EwINIeEQxKWXXjp1XXPOOafr16+fLxs5cqQnm4MHD3Zjx451zz77rNtnn318HuEoH3/8sT8eNGiQe/jhh91ll13mFllkEZ9nnRNrHifhjL3KKqu4e++9111++eW+7s9//nNf/YQTTvDn119/vXviiSfcmmuu6QkyhZVIOHHstqaJEyf6kBXO+RCO8r//+79u/vnnd4cffrh75pln3PHHH+/L7r77bjdhwgR3yCGH+PPzzz/fk/BK8wCTeeed1z3//PPu9ddfdxB+SDkJfBhzr7328uOMGDHCn3P3IG0c30h/hIAQEAJthoDp07RpyUbc42Qj0iRDeUKg6yPQEhK+2GKLeSSNhD/99NMRsnESjvcZZX311VdH5VtuuaXPs4w0En7mmWdasY8vN8+7ZXKL77HHHnPEn9M/qRIJv/nmm309fgRYsnnEY8K/++479+qrrzrINv1C9km2zmRMeNo8eNiTttwRuOKKK3x/NiZ3ASj74IMPfMgLoTicM16lcay9voWAEBAC7YAAequSo0Y24oerJBvRDtKqOQiB1iHQEBK++OKLe3KYnDahFijfDTbYwBcZOY3HN8dJ+AUXXODrE2Ziyby/dp5GwiGvlggBMRKOZxmv+RxzzOFWW201t+2220bzrETCCQFh3oS5WDKybCQcb/d8883nuM3KLjDU/+Mf/+ir2zqNhFeax/vvv++GDh3q29MHn1133dX3gwecc9ZsH9Ziu8Mkx7G56lsICAEh0E4IyEbIRrSTPGouQqBdEGgICWf7Psji6aefXrIuwjXIP+uss3y+kUYeQrQUJ+F/+tOffH3inS2ts846Ps/O00j4VVddZcUuTsK32GILH+rBjwGSkVqOK5HwW265xY958cUXR/3SF2uBhFvYCx5zEnHflDF/kq3zq6++8ueV5kEFSDqhODfccIMbPny47wvPvT3YSmw9CS8J3ndLyXEsX99CQAgIgXZCQDZCNqKd5FFzEQLtgkBDSPhHH33kH56EiO6yyy7ulFNOibzOxGtbMtJYjoRDMCHZbFkIcT/ggANc9+7dPSm1Pmoh4RD4WWed1cdbExPOg43MkVSJhH/zzTe+3oABAzzBhozbQ5qQcH4k0A/5eLK33357f27hKBYTDiknTrzSPDbffHPflvkQbnLUUUf589dee809+uij/pi7AZxTxnruuOMOv4bkOIaRvoWAEBAC7YSAbIRsRDvJo+YiBNoFgYaQcBZDbPRWW23lSSMEld1SIOQffvhhtFZIOJ7qOAknFpo82yecUJSBAwd68g353G233Xyf1gkPecYfzISUx/f6ptzCUW677Ta/XzfzgVCPHz/ek3weeIQcs5d3vK2NwTde7h49evixIdE8SEp9SDgkfe211/Zl7IQCKeeHAySZdOONN0Y4EFdeaR5sz7jppptG9dnB5eyzz46mwo8R8lgDHx4CtZQcx/L1LQSEgBBoNwRkI2Qj2k0mNR8h0NkINIyE20IgqRDLrG/AtHZ8s0MI8d3sSGJphx128CTUzvN8WzhHnrZTpkwp26xSGUSdEJN4qjQP4scrlfNwZlpKGyetnvKEgBAQAu2AgGzED1chTXdXsgGyEe0gvZqDEGgsAg0n4fVMDyUz++yze48vDx/a3ty2B3c9fautEBACQkAIhI2AbETY10+zFwJCoBSBtiLhTI39wXfffXcfR82uKrzQJ/lGytIl6EwICAEhIASKgoBsRFGutNYpBLo+Am1Hwrs+5FqhEBACQkAICAEhIASEQNEREAkvugRo/UJACAgBISAEhIAQEAItR0AkvOWQa0AhIASEgBAQAkJACAiBoiMgEl50CdD6hYAQEAJCQAgIASEgBFqOgEh4yyHXgEJACAgBISAEhIAQEAJFR0AkvOgSoPULASEgBISAEBACQkAItBwBkfCWQ64BhYAQEAJCQAgIASEgBIqOgEh40SVA6xcCQkAICAEhIASEgBBoOQIi4S2HXAMKASEgBISAEBACQkAIFB0BkfCiS4DWLwSEgBAQAkJACAgBIdByBETCWw65BhQCQkAICAEhIASEgBAoOgL/H61N9lsGDPG9AAAAAElFTkSuQmCC)

# In[ ]:


# Conteo de clases
count_class_0, count_class_1 = df3.ventaPrestDig.value_counts()


# In[ ]:


# Dividiendo los sets por clases
df_class_0 = df3[df3['ventaPrestDig'] == 0]
df_class_1 = df3[df3['ventaPrestDig'] == 1]


# In[ ]:


print('Cantidades por fila de clase:')
print(df_class_0.shape)
print(df_class_1.shape)


# In[ ]:





# #### 3.1. Random under-sampling (Submuestreo aleatorio)

# In[ ]:


df_class_0_under = df_class_0.sample(count_class_1)
df_under = pd.concat([df_class_0_under,df_class_1],axis = 0)


# In[ ]:


print('Dimensión por tipo de clases generadas:')
print('dim df_class_0_under:',df_class_0_under.shape)
print('dim df_under:',df_under.shape)


# In[ ]:


print('Random under-sampling:')
print(df_under.ventaPrestDig.value_counts())


# In[ ]:


df_under.ventaPrestDig.value_counts().plot(kind='bar', title='Count (ventaPrestDig)');


# In[ ]:





# ## Probando la predicción con data balanceada

# In[ ]:


# Separación de predictoras y predicha
# DataSet:df_under


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#! pip install woe


# In[ ]:


# Anexos : WOE
import woe
from woe.eval import plot_ks
import pandas.core.algorithms as algos
from pandas import Series
import scipy.stats.stats as stats
import re
import traceback
import string
import os
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import rcParams
rcParams['figure.figsize'] = 14, 8
import warnings
warnings.filterwarnings('ignore')
max_bin = 20
force_bin = 3


# Creamos las Woes - IV
max_bin = 20
force_bin = 3

def mono_bin(Y, X, n = max_bin):
    df1 = pd.DataFrame({"X": X, "Y": Y})
    justmiss = df1[['X','Y']][df1.X.isnull()]
    notmiss = df1[['X','Y']][df1.X.notnull()]
    r = 0
    while np.abs(r) < 1:
        try:
            d1 = pd.DataFrame({"X": notmiss.X, "Y": notmiss.Y, "Bucket": pd.qcut(notmiss.X, n)})
            d2 = d1.groupby('Bucket', as_index=True)
            r, p = stats.spearmanr(d2.mean().X, d2.mean().Y)
            n = n - 1 
        except Exception as e:
            n = n - 1

    if len(d2) == 1:
        n = force_bin         
        bins = algos.quantile(notmiss.X, np.linspace(0, 1, n))
        if len(np.unique(bins)) == 2:
            bins = np.insert(bins, 0, 1)
            bins[1] = bins[1]-(bins[1]/2)
        d1 = pd.DataFrame({"X": notmiss.X, "Y": notmiss.Y, "Bucket": pd.cut(notmiss.X, np.unique(bins),include_lowest=True)}) 
        d2 = d1.groupby('Bucket', as_index=True)
    
    d3 = pd.DataFrame({},index=[])
    d3["MIN_VALUE"] = d2.min().X
    d3["MAX_VALUE"] = d2.max().X
    d3["COUNT"] = d2.count().Y
    d3["EVENT"] = d2.sum().Y
    d3["NONEVENT"] = d2.count().Y - d2.sum().Y
    d3=d3.reset_index(drop=True)
    
    if len(justmiss.index) > 0:
        d4 = pd.DataFrame({'MIN_VALUE':np.nan},index=[0])
        d4["MAX_VALUE"] = np.nan
        d4["COUNT"] = justmiss.count().Y
        d4["EVENT"] = justmiss.sum().Y
        d4["NONEVENT"] = justmiss.count().Y - justmiss.sum().Y
        d3 = d3.append(d4,ignore_index=True)
    
    d3["EVENT_RATE"] = d3.EVENT/d3.COUNT
    d3["NON_EVENT_RATE"] = d3.NONEVENT/d3.COUNT
    d3["DIST_EVENT"] = d3.EVENT/d3.sum().EVENT
    d3["DIST_NON_EVENT"] = d3.NONEVENT/d3.sum().NONEVENT
    d3["WOE"] = np.log(d3.DIST_EVENT/d3.DIST_NON_EVENT)
    d3["IV"] = (d3.DIST_EVENT-d3.DIST_NON_EVENT)*np.log(d3.DIST_EVENT/d3.DIST_NON_EVENT)
    d3["VAR_NAME"] = "VAR"
    d3 = d3[['VAR_NAME','MIN_VALUE', 'MAX_VALUE', 'COUNT', 'EVENT', 'EVENT_RATE', 'NONEVENT', 'NON_EVENT_RATE', 'DIST_EVENT','DIST_NON_EVENT','WOE', 'IV']]       
    d3 = d3.replace([np.inf, -np.inf], 0)
    d3.IV = d3.IV.sum()
    
    return(d3)


def char_bin(Y, X):
        
    df1 = pd.DataFrame({"X": X, "Y": Y})
    justmiss = df1[['X','Y']][df1.X.isnull()]
    notmiss = df1[['X','Y']][df1.X.notnull()]    
    df2 = notmiss.groupby('X',as_index=True)
    
    d3 = pd.DataFrame({},index=[])
    d3["COUNT"] = df2.count().Y
    d3["MIN_VALUE"] = df2.sum().Y.index
    d3["MAX_VALUE"] = d3["MIN_VALUE"]
    d3["EVENT"] = df2.sum().Y
    d3["NONEVENT"] = df2.count().Y - df2.sum().Y
    
    if len(justmiss.index) > 0:
        d4 = pd.DataFrame({'MIN_VALUE':np.nan},index=[0])
        d4["MAX_VALUE"] = np.nan
        d4["COUNT"] = justmiss.count().Y
        d4["EVENT"] = justmiss.sum().Y
        d4["NONEVENT"] = justmiss.count().Y - justmiss.sum().Y
        d3 = d3.append(d4,ignore_index=True)
    
    d3["EVENT_RATE"] = d3.EVENT/d3.COUNT
    d3["NON_EVENT_RATE"] = d3.NONEVENT/d3.COUNT
    d3["DIST_EVENT"] = d3.EVENT/d3.sum().EVENT
    d3["DIST_NON_EVENT"] = d3.NONEVENT/d3.sum().NONEVENT
    d3["WOE"] = np.log(d3.DIST_EVENT/d3.DIST_NON_EVENT)
    d3["IV"] = (d3.DIST_EVENT-d3.DIST_NON_EVENT)*np.log(d3.DIST_EVENT/d3.DIST_NON_EVENT)
    d3["VAR_NAME"] = "VAR"
    d3 = d3[['VAR_NAME','MIN_VALUE', 'MAX_VALUE', 'COUNT', 'EVENT', 'EVENT_RATE', 'NONEVENT', 'NON_EVENT_RATE', 'DIST_EVENT','DIST_NON_EVENT','WOE', 'IV']]      
    d3 = d3.replace([np.inf, -np.inf], 0)
    d3.IV = d3.IV.sum()
    d3 = d3.reset_index(drop=True)
    
    return(d3)


def data_vars(df1, target):
    
    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-2]
    vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
    final = (re.findall(r"[\w']+", vars_name))[-1]
    
    x = df1.dtypes.index
    count = -1
    
    for i in x:
        if i.upper() not in (final.upper()):
            if np.issubdtype(df1[i], np.number) and len(Series.unique(df1[i])) > 2:
                conv = mono_bin(target, df1[i])
                conv["VAR_NAME"] = i
                count = count + 1
            else:
                conv = char_bin(target, df1[i])
                conv["VAR_NAME"] = i            
                count = count + 1
                
            if count == 0:
                iv_df = conv
            else:
                iv_df = iv_df.append(conv,ignore_index=True)
    
    iv = pd.DataFrame({'IV':iv_df.groupby('VAR_NAME').IV.max()})
    iv = iv.reset_index()
    return(iv_df,iv)


# In[ ]:


import numpy as np
import pandas as pd
import graphviz, IPython
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.ticker import FuncFormatter
from sklearn.tree import export_graphviz

def draw_tree(tree, df):
    s = export_graphviz(tree, out_file=None, feature_names=df.columns, filled=True)
    return graphviz.Source(s)

def set_rf_samples(n):
    """ Changes Scikit learn's random forests to give each tree a random sample of
    n random rows.
    """
    forest._generate_sample_indices = (lambda rs, n_samples:
        forest.check_random_state(rs).randint(0, n_samples, n))

def reset_rf_samples():
    """ Undoes the changes produced by set_rf_samples.
    """
    forest._generate_sample_indices = (lambda rs, n_samples:
        forest.check_random_state(rs).randint(0, n_samples, n_samples))

# Based on https://github.com/chrispaulca/waterfall.git
def waterfallplot(sample, data, Title="", x_lab="", y_lab="",
		 formatting="{:,.1f}", green_color='#29EA38', red_color='#FB3C62', blue_color='#24CAFF',
		 sorted_value=False, threshold=None, other_label='other', net_label='net', 
		 rotation_value=0, size=None):
	'''
	Given two sequences ordered appropriately, generate a standard waterfall chart.
	Optionally modify the title, axis labels, number formatting, bar colors, 
	increment sorting, and thresholding. Thresholding groups lower magnitude changes
	into a combined group to display as a single entity on the chart.
	'''
	
	#convert data and index to np.array
	index = np.array([f'{c}\n({sample[c].iloc[0]})' for c in sample])
	data = np.array(data)
	
	# wip
	#sorted by absolute value 
	if sorted_value: 
		abs_data = abs(data)
		data_order = np.argsort(abs_data)[::-1]
		data = data[data_order]
		index = index[data_order]
	
	#group contributors less than the threshold into 'other' 
	if threshold:
		
		abs_data = abs(data)
		threshold_v = abs_data.max()*threshold
		
		if threshold_v > abs_data.min():
			index = np.append(index[abs_data>=threshold_v],other_label)
			data = np.append(data[abs_data>=threshold_v],sum(data[abs_data<threshold_v]))
	
	changes = {'amount' : data}
	
	#define format formatter
	def money(x, pos):
		'The two args are the value and tick position'
		return formatting.format(x)
	formatter = FuncFormatter(money)
	
	fig, ax = plt.subplots(figsize=size)
	ax.yaxis.set_major_formatter(formatter)

	#Store data and create a blank series to use for the waterfall
	trans = pd.DataFrame(data=changes,index=index)
	blank = trans.amount.cumsum().shift(1).fillna(0)
	
	trans['positive'] = trans['amount'] > 0

	#Get the net total number for the final element in the waterfall
	total = trans.sum().amount
	trans.loc[net_label]= total
	blank.loc[net_label] = total

	#The steps graphically show the levels as well as used for label placement
	step = blank.reset_index(drop=True).repeat(3).shift(-1)
	step[1::3] = np.nan

	#When plotting the last element, we want to show the full bar,
	#Set the blank to 0
	blank.loc[net_label] = 0
	
	#define bar colors for net bar
	trans.loc[trans['positive'] > 1, 'positive'] = 99
	trans.loc[trans['positive'] < 0, 'positive'] = 99
	trans.loc[(trans['positive'] > 0) & (trans['positive'] < 1), 'positive'] = 99
	
	trans['color'] = trans['positive']
	
	trans.loc[trans['positive'] == 1, 'color'] = green_color
	trans.loc[trans['positive'] == 0, 'color'] = red_color
	trans.loc[trans['positive'] == 99, 'color'] = blue_color
	
	my_colors = list(trans.color)
	
	#Plot and label
	my_plot = plt.bar(range(0,len(trans.index)), blank, width=0.5, color='white')
	plt.bar(range(0,len(trans.index)), trans.amount, width=0.6,
			 bottom=blank, color=my_colors)       
								   
	
	# connecting lines - figure out later
	#my_plot = lines.Line2D(step.index, step.values, color = "gray")
	#my_plot = lines.Line2D((3,3), (4,4))
	
	#axis labels
	plt.xlabel("\n" + x_lab)
	plt.ylabel(y_lab + "\n")

	#Get the y-axis position for the labels
	y_height = trans.amount.cumsum().shift(1).fillna(0)
	
	temp = list(trans.amount)
	
	# create dynamic chart range
	for i in range(len(temp)):
		if (i > 0) & (i < (len(temp) - 1)):
			temp[i] = temp[i] + temp[i-1]
	
	trans['temp'] = temp
			
	plot_max = trans['temp'].max()
	plot_min = trans['temp'].min()
	
	#Make sure the plot doesn't accidentally focus only on the changes in the data
	if all(i >= 0 for i in temp):
		plot_min = 0
	if all(i < 0 for i in temp):
		plot_max = 0
	
	if abs(plot_max) >= abs(plot_min):
		maxmax = abs(plot_max)   
	else:
		maxmax = abs(plot_min)
		
	pos_offset = maxmax / 40
	
	plot_offset = maxmax / 15 ## needs to me cumulative sum dynamic

	#Start label loop
	loop = 0
	for index, row in trans.iterrows():
		# For the last item in the list, we don't want to double count
		if row['amount'] == total:
			y = y_height[loop]
		else:
			y = y_height[loop] + row['amount']
		# Determine if we want a neg or pos offset
		if row['amount'] > 0:
			y += (pos_offset*2)
			plt.annotate(formatting.format(row['amount']),(loop,y),ha="center", color = 'g', fontsize=9)
		else:
			y -= (pos_offset*4)
			plt.annotate(formatting.format(row['amount']),(loop,y),ha="center", color = 'r', fontsize=9)
		loop+=1

	#Scale up the y axis so there is room for the labels
	plt.ylim(plot_min-round(3.6*plot_offset, 7),plot_max+round(3.6*plot_offset, 7))
	
	#Rotate the labels
	plt.xticks(range(0,len(trans)), trans.index, rotation=rotation_value)
	
	#add zero line and title
	plt.axhline(0, color='black', linewidth = 0.6, linestyle="dashed")
	plt.title(Title)
	plt.tight_layout()

	return plt

