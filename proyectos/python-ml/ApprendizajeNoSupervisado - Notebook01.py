#!/usr/bin/env python
# coding: utf-8

# In[ ]:


################################################################################
########## ------- Machine Learning Inmersion ------------######################
################################################################################
#### Capacitador: André Omar Chávez Panduro
#### email: andre.chavez@urp.edu.pe
#### Tema: Reducción de Dimensiones / Segmentacion Clientes
#### version: 2.0
###############################################################################


# In[ ]:


# Conexion a Google Colaborative
from google.colab import drive
drive.mount('/gdrive')


# In[ ]:


#Importar las librerías necesarias en Python.
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:





# In[ ]:


# Lectura de los datos!


# In[ ]:


data = pd.read_csv('')


# In[ ]:





# In[ ]:


# Dimension de los datos!
data.shape


# In[ ]:





# In[ ]:


# Tenemos un dataset de indicadores del milenio!
data.head()


# In[ ]:





# In[ ]:


# Revisamos las columnas y entendemos un poco los datos!
data.columns


# In[ ]:


# Dimensiones de la data
data.isnull().sum()


# In[ ]:


# Vemos el % de Valores perdidos por variables
data.isnull().sum()/data.shape[0]


# In[ ]:





# In[ ]:


# Vista de las columnas totales del set de datos!
ColumnasTotales = data.columns.tolist()


# In[ ]:


# Columnas no input!
columnas_no_input = ['country','region']


# In[ ]:





# In[ ]:





# In[ ]:


# Me quedo con las columnas necesarias
columnas_complemento = [x for x in ColumnasTotales if x not in columnas_no_input]


# In[ ]:


columnas_complemento


# In[ ]:


# Completitud de los datos!


# In[ ]:


# Usamos los metodos de imputacion aprendidos!
from sklearn.impute import SimpleImputer
# Generamos el imputador iterativo - Imputacion Univariada Numerica
imp_univ_num = SimpleImputer(missing_values=np.nan, strategy='median')


# In[ ]:


data_impt_num = data[columnas_complemento]


# In[ ]:





# In[ ]:





# In[ ]:


# Realizamos la imputación univariada en una nueva base de datos - Variables Numericas
imp_univ_num.fit(data_impt_num)
data_imp = pd.DataFrame(data=imp_univ_num.transform(data_impt_num), 
                             columns=data_impt_num.columns,dtype='float')


# In[1]:


# Lo importante es que tenemos completitud de los datos!
data_imp.head()


# In[ ]:





# In[1]:


# Analizamos la relación existente entre las variables
from scipy.stats.stats import pearsonr  
from scipy.spatial.distance import cdist
data_imp.corr()


# In[ ]:


# Exportamos la información a un csv para poder visualizar las relaciones.
matrix_correlations_paises.to_csv('')


# In[ ]:





# In[1]:


## Analisis de Componentes Principales ##
data_imp.shape # Dimension es 207 filas y 12 variables!
# Objetivo : Podemos representar los 207 paises en menos de 12 variables?


# In[ ]:





# In[ ]:


# Escalamos los datos!
from sklearn.preprocessing import scale
X = scale(data_imp)


# In[ ]:





# In[1]:


# Revisamos la informacion!
pd.DataFrame(X, index=data_imp.index, columns=data_imp.columns).head()


# In[ ]:


# Porque escalar ?
# Numero de hijos : [0 - 10]
# Ingreso         : [830 - 20000]


# In[ ]:


# Aplicamos el Analisis de Componentes Principales!


# In[ ]:


from sklearn.decomposition import PCA
pca = PCA(n_components=4) # Instancio o codificas
pca = pca.fit(X)          # Tenemos el ACP ejecutado


# In[1]:


# Autovalores asocados a cada Componente Principal!
explained_variance = pca.explained_variance_
print('Varianza explicada por cada componente principal:')
print(explained_variance)


# In[ ]:


# Criterio de Kaiser!


# In[ ]:


# Con cuántas nuevas variables me voy a quedar?
# Me quedaria con 4 variables! 
# De 12 variables --> 4 variables!


# In[1]:


# Varianza Acumulada por cada CP!
PVE = pca.explained_variance_ratio_
print('Proporción de varianza explicada (PVE) por cada componente principal:')
print(PVE)


# In[ ]:





# In[1]:


# Criterio de la Varianza Explicada!
np.cumsum(pca.explained_variance_ratio_)


# In[ ]:





# In[1]:


# Graficamos la explicación de la varianza por cada CP.
plt.figure(figsize=(7,5))
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], pca.explained_variance_ratio_, '-o')
plt.ylabel('Proporción de Varianza Explicada')
plt.xlabel('Componente Principal')
plt.xlim(0.75,4.25)
plt.ylim(0,1.05)
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.show()


# In[ ]:





# In[1]:


# Graficamos la explicación de la varianza acumulada por cada CP.
plt.figure(figsize=(7,5))
plt.plot([1,2,3,4], np.cumsum(pca.explained_variance_ratio_), '-s')
plt.ylabel('Proporción Acumulada de Varianza Explicada')
plt.xlabel('Componente Principal')
plt.xlim(0.75,4.25)
plt.ylim(0,1.05)
plt.xticks([1,2,3,4])
plt.show()


# In[ ]:


# Tomamos una decision!


# In[ ]:


# Debido a que ya decidimos con cuantos componentes quedarnos volvemos a realizar el analisis!


# In[ ]:


from sklearn.decomposition import PCA


# In[ ]:


pca = PCA(n_components=4) # Instancio o codificas
pca = pca.fit(X)          # Tenemos el ACP ejecutado


# In[ ]:





# In[ ]:


# Hallamos las cargas factoriales!
# Explicacion!
pca_loadings = pca.components_


# In[ ]:





# In[1]:


# Mostramos las cargas factoriales de cada componente principal en un DataFrame
pd.DataFrame(pca_loadings, columns=data_imp.columns, index=['PC1', 'PC2', 'PC3','PC4']).head(7)


# In[ ]:





# In[ ]:


# Usando sklearn
pca_scores = pca.transform(X) # Puntuaciones factoriales


# In[ ]:





# In[ ]:


df_plot = pd.DataFrame(pca_scores, columns=['PC1', 'PC2', 'PC3','PC4'], index=data_imp.index)


# In[1]:


df_plot.head()


# In[1]:


df_plot.shape


# In[ ]:


# Graficamos las variables y su relacion con los CP.


# In[1]:


biplot(loadings=pca_loadings, scores=pca_scores, index=data_imp.index, columns=data_imp.columns)


# In[ ]:





# In[ ]:


# Fin!


# In[ ]:





# In[ ]:


# Segmentación o Cluster de países del mundo!


# In[1]:


# Usamos el algoritmo de K-Means ++
from sklearn.cluster import KMeans
km = KMeans(3, 
            init='k-means++', 
            random_state = 3425) 


# In[1]:


# Ajustamos o aplicamos el k-means!
km.fit(df_plot)


# In[ ]:





# In[ ]:


# Encontramos o hallamos el segmento por o cluster por pais!
SegmentoPais = km.predict(df_plot)


# In[2]:


# Agregamos la variable al set de datos!
data_imp.head(3)


# In[ ]:


data_imp['SegmentoPais'] = SegmentoPais


# In[2]:


# Cantidad de elementos por grupo
data_imp.groupby('SegmentoPais').contraception.count()


# In[2]:


# Siempre le debemos poner un nombre al grupo o cluster de acuerdo a las características que tiene!
clust_map = {
    0:'Cluster0',
    1:'Cluster1',
    2:'Cluster2'}

data_imp.SegmentoPais = data_imp.SegmentoPais.map(clust_map)


# In[ ]:





# In[ ]:


# Analizamos las variables, sus asociaciones y representaciones en los cluster!


# In[2]:


# Establecemos los colores de los cluster!
d_color = {
    'Cluster0':'yellow',
    'Cluster1':'red',
    'Cluster2':'green'}


# In[ ]:





# In[2]:


# Grafico de las variables, asociaciones y cluster!
fig, ax = plt.subplots()
for clust in clust_map.values():
    color = d_color[clust]
    data_imp[data_imp.SegmentoPais == clust].plot(kind='scatter', x='GDPperCapita', y='infantMortality', label=clust, ax=ax, color=color)
handles, labels = ax.get_legend_handles_labels()
_ = ax.legend(handles, labels, loc="upper right")


# In[ ]:





# In[2]:


# Grafico de las variables, asociaciones y cluster!
fig, ax = plt.subplots()
for clust in clust_map.values():
    color = d_color[clust]
    data_imp[data_imp.SegmentoPais == clust].plot(kind='scatter', x='GDPperCapita', y='lifeMale', label=clust, ax=ax, color=color)
handles, labels = ax.get_legend_handles_labels()
_ = ax.legend(handles, labels, loc="lower right")


# In[ ]:





# In[2]:


# Grafico de las variables, asociaciones y cluster!
fig, ax = plt.subplots()
for clust in clust_map.values():
    color = d_color[clust]
    data_imp[data_imp.SegmentoPais == clust].plot(kind='scatter', x='GDPperCapita', y='lifeFemale', label=clust, ax=ax, color=color)
handles, labels = ax.get_legend_handles_labels()
_ = ax.legend(handles, labels, loc="lower right")


# In[ ]:





# In[2]:


# Validacion de nuestro cluster!
from sklearn import metrics
from sklearn import metrics

# Obtenemos los indicadores de clustering:
print('Inercia: '+str(km.inertia_)) 
print('Silueta: '+str(metrics.silhouette_score(df_plot, SegmentoPais, metric='euclidean')))


# In[ ]:





# In[ ]:


# Resumen Metodologico

 # X (207,12)    ---- >     Z (207,4) ACP      --- ----> Y (Cluster)
 # X,Y (207,13)    ---- >   Z,Y (207,5) ACP  --- ----> Y (Clasificacion, Regresion)
 # Perfilamiento!
 # X , Y


# In[2]:


data_imp.head(5)


# In[ ]:


# Fin!


# In[ ]:





# In[ ]:


# Anexos!
def biplot(loadings, scores, index, columns):
    fig , ax1 = plt.subplots(figsize=(9,7))

    ax1.set_xlim(-3.5,3.5)
    ax1.set_ylim(-3.5,3.5)

    # Nombre de cada estado ubicado por puntajes para cada componente principal
    for i, index in enumerate(index):
        ax1.annotate(index, (scores[i, 0], scores[i, 1]), ha='center', color='blue')

    # Líneas de referencia
    ax1.hlines(0,-3.5,3.5, linestyles='dotted', colors='grey')
    ax1.vlines(0,-3.5,3.5, linestyles='dotted', colors='grey')

    ax1.set_xlabel('Primer Componente Principal')
    ax1.set_ylabel('Segundo Componente Principal')

    # Diagramar los vectores de cargas, superponiendo un segundo eje x, y
    ax2 = ax1.twinx().twiny() 

    ax2.set_ylim(-1,1)
    ax2.set_xlim(-1,1)
    ax2.set_xlabel('Vectores de cargas de los componentes principales', color='red')

    # Vectores de carga
    # La variable 'a' es un pequeño offset para separar las etiquetas de las flechas
    a = 1.07  
    for i, column in enumerate(columns):
        ax2.annotate(column, (loadings[0,i]*a, loadings[1,i]*a), color='red')
        ax2.arrow(0, 0, loadings[0,i], loadings[1,i], color='red')
    plt.show()

