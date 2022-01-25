#!/usr/bin/env python
# coding: utf-8

# 
# # DMC - Python for Analytics - Sesión 06
# Profesor: Manuel Montoya | Data Scientist @ Belcorp

# In[134]:


from google.colab import drive

drive.mount("/content/drive")


# In[135]:


import pandas
import numpy
import os

from sklearn.cluster import KMeans
from sklearn import preprocessing 
from sklearn.decomposition import PCA

import seaborn
import matplotlib.pyplot as plt


# In[136]:


path_base = '/content/drive/My Drive/python-for-analytics/sesion-06/data'
os.listdir(path_base)


# # Kmeans

# Mall Customer Data https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python

# In[137]:


df_customers = pandas.read_csv(f"{path_base}/mall-customers.csv")
df_customers.head()


# In[138]:


df_customers = df_customers.drop("CustomerID", axis = 1)
df_customers.head()


# In[139]:


df_customers.info()


# In[140]:


df_customers.describe()


# In[141]:


df_customers["Gender"] = df_customers["Gender"].apply(lambda value: 1 if value == "Female" else 0)


# In[142]:


df_customers.head()


# In[161]:


model = KMeans(n_clusters = 3)
model.fit(df_customers)


# In[162]:


model.predict(df_customers)


# In[163]:


df_customers["cluster1"] = model.predict(df_customers)
df_customers.head()


# In[164]:


plt.scatter(df_customers["Age"], df_customers["Annual Income (k$)"], c = df_customers["cluster1"])
plt.ylabel("Annual Income")
plt.xlabel("Age")


# In[165]:


plt.scatter(df_customers["Age"], df_customers["Spending Score (1-100)"], c = df_customers["cluster1"])
plt.ylabel("Spending Score (1-100)")
plt.xlabel("Age")


# In[166]:


plt.scatter(df_customers["Annual Income (k$)"], df_customers["Spending Score (1-100)"], c = df_customers["cluster1"])
plt.ylabel("Spending Score (1-100)")
plt.xlabel("Annual Income (k$)")


# # Preprocesamiento de variables

# In[167]:


df_customers = df_customers.drop("cluster1", axis = 1)
df_customers.head()


# In[168]:


df_scaled = pandas.DataFrame(preprocessing.scale(df_customers),columns = df_customers.columns) 
df_scaled.head()


# In[170]:


df_customers.describe()


# In[169]:


df_scaled.describe()


# In[171]:


seaborn.distplot(df_customers["Age"])


# In[172]:


seaborn.distplot(df_scaled["Age"])


# In[173]:


seaborn.distplot(df_scaled["Annual Income (k$)"])


# # Análisis de componentes principales (PCA)

# In[174]:


pca = PCA(n_components = 2)


# In[177]:


df_scaled.head()


# In[176]:


pca.fit(df_scaled)
pca.transform(df_scaled)[:5]


# In[178]:


pca.components_


# In[180]:


index = [f'PC-{i}' for i in range(2)]
df_factors = pandas.DataFrame(pca.components_,columns=df_scaled.columns,index = index).T
df_factors


# In[179]:


pca_factors = pca.transform(df_scaled)
pca_factors[:5]


# In[181]:


pca.explained_variance_ratio_


# In[182]:


numpy.sum(pca.explained_variance_ratio_)


# In[183]:


plt.scatter(pca_factors[:,0], pca_factors[:,1])


# # KMeans

# Documentación https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

# In[190]:


model = KMeans(n_clusters = 3)
model.fit(pca_factors)
clusters = model.predict(pca_factors)


# In[191]:


plt.scatter(pca_factors[:,0], pca_factors[:,1], c = clusters)
plt.ylabel("Factor 2")
plt.xlabel("Factor 1")


# In[192]:


df_customers["clusters_pca"] = clusters


# In[193]:


df_customers.head()


# In[194]:


df_customers.groupby("clusters_pca").mean()


# In[195]:


df_customers.groupby("clusters_pca").count()


# # Método del codo

# In[196]:


df_scaled.head()


# In[198]:


components = list(range(1,5))
total_variance = []

for n_components in components:
    
    pca = PCA(n_components = n_components)
    pca.fit(df_scaled)
    
    variance_components = numpy.sum(pca.explained_variance_ratio_)
    total_variance.append(variance_components)
    
    print(f"Total variance {n_components}: {variance_components}")
    
    
plt.figure(figsize=(16,8))
plt.plot(components, total_variance, 'bx-')
plt.xlabel('n_componends')
plt.ylabel('variance')
plt.title('Elbow method to determine number of components')
plt.show()


# Se van a elegir tres factores principales para el análisis

# In[199]:


pca = PCA(n_components = 3)
pca.fit(df_scaled)
pca_factors = pca.transform(df_scaled)


# In[200]:


pca_factors[:5]


# In[201]:


clusters = list(range(1,21))
total_inertia = []

for n_clusters in clusters:
    
    model = KMeans(n_clusters = n_clusters)
    model.fit(pca_factors)
    
    inertia_model = model.inertia_
    total_inertia.append(inertia_model)
    
    print(f"Total inertia{n_clusters}: {inertia_model}")
    
    
plt.figure(figsize=(16,8))
plt.plot(clusters, total_inertia, 'bx-')
plt.xlabel('n_clusters')
plt.ylabel('inertia')
plt.title('Elbow method to determine number of clusters')
plt.show()


# In[202]:


model = KMeans(n_clusters = 4)
model.fit(pca_factors)
clusters = model.predict(pca_factors)

df_customers["clusters_pca"] = clusters


# In[203]:


fig = plt.figure(figsize = (12,12))
ax = fig.add_subplot(111, projection='3d')


ax.scatter(pca_factors[:,0], pca_factors[:,1], pca_factors[:,2], c = clusters)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


# # Descriptivos de clusters

# In[204]:


df_customers.head()


# In[205]:


df_customers.groupby("clusters_pca").mean()


# In[206]:


df_customers[["Age", "clusters_pca"]].boxplot(by = "clusters_pca")


# In[208]:


df_customers[["Annual Income (k$)", "clusters_pca"]].boxplot(by = "clusters_pca")


# In[209]:


df_customers[["Spending Score (1-100)", "clusters_pca"]].boxplot(by = "clusters_pca")


# # Otros algoritmos

# In[210]:


from sklearn.cluster import AgglomerativeClustering


# In[211]:


pca = PCA(n_components = 2)
pca.fit(df_scaled)
pca_factors = pca.transform(df_scaled)


# In[212]:


model = KMeans(n_clusters = 3)
model.fit(pca_factors)
clusters = model.predict(pca_factors)

plt.scatter(pca_factors[:,0], pca_factors[:,1], c = clusters)


# In[213]:


model = AgglomerativeClustering(n_clusters = 3)
model.fit(df_scaled)
clusters = model.labels_


# In[214]:


plt.scatter(pca_factors[:,0], pca_factors[:,1], c = clusters)


# In[ ]:




