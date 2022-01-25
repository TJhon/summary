#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#########################################################################
#########------- Machine Learning Inmersion ------------#################
#########################################################################
# Capacitador: André Omar Chávez Panduro
# email: andre.chavez@urp.edu.pe
# Tema:  Aprendizaje Supervisado Respuesta Categorica
# version: 1.0
#########################################################################


# In[ ]:


# Conexion a Google Colaborative
from google.colab import drive
drive.mount('/gdrive')


# In[ ]:


##################################################
## Desarrollo de Modelos de Machine Learning
##################################################


# ### **1. Carga de Modulos**

# In[2]:


#Importar las librerías necesarias en Python.
import pandas as pd ## Manejo de dataframes o set de datos
import warnings
warnings.filterwarnings("ignore")
import numpy as np ## Todo lo referente a trabajar con vectores y matrices
from scipy import stats ## Herramientas y algoritmos matemáticos para python


# In[ ]:


## Leemos los datos o el dataset a trabajar


# ### **2. Lectura Inicial de base de datos**

# #### 2.1. Carga de datos

# In[3]:


# Leemos la data de desarrollo de modeolos
desarrll = pd.read_csv("") # Ruta donde esta su set de datos!
# Leer el dataset en un dataframe usando pandas


# In[5]:


# Vemos la dimensionalidad


# In[6]:


# Visualizacion Global de los datos
desarrll.head()


# #### 2.2. Buenas prácticas

# In[ ]:


desarrll.columns


# In[8]:


# Renombramos las variables por buenas prácticas

desarrll.columns = Columnsnames


# #### 2.3. AED

# In[8]:


desarrll.describe(include='all') # Describir todas las variables.


# In[ ]:





# ### **3. Tratamientos o Recodificacion de variables**

# #### 3.1. Completitud de los datos

# In[9]:


# Revisamos los valores nulos o missings!


# In[11]:


# No olvidemos separar las variables cualitativas para poder trabajarlas eficientemente
columnas_categoricas = ["Gender","Married","Education","Self_Employed","Property_Area","Dependents",'Credit_History',"Loan_Status"]
columnas_numericas   = ["ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term"]


# In[ ]:





# In[10]:


# Usamos los metodos de imputacion aprendidos!
from sklearn.impute import SimpleImputer
# Generamos el imputador iterativo - Imputacion Univariada Numerica
imp_univ_num = SimpleImputer(missing_values=np.nan, strategy='mean')

# Generamos el imputador iterativo - Imputacion Univariada Categorica
imp_univ_cat = 


# In[13]:


# Generamos los subset de variables categoricas - continuas!


# In[15]:


# Realizamos la imputación univariada en una nueva base de datos - Variables Numericas
imp_univ_num.fit(data_impt_num)
imputed_data_univ_num = pd.DataFrame(data=imp_univ_num.transform(data_impt_num), 
                             columns=data_impt_num.columns,dtype='float')

# Realizamos la imputación univariada en una nueva base de datos - Variables Categoricas
imp_univ_cat.fit(data_impt_cat)
imputed_data_univ_cat = pd.DataFrame(data=imp_univ_cat.transform(data_impt_cat), 
                             columns=data_impt_cat.columns,dtype='object')


# In[17]:


# Consolidamos los subset!


# In[ ]:


# Comprobamos la completitud de los datos!


# #### 3.2. Recodificacion de los datos

# In[17]:


# LabelEncoder de los datos!
from sklearn.preprocessing import LabelEncoder
# Preprocesamiento con LabelEncoderfrom 
for c in columnas_categoricas:
    print(str(c))
    le = LabelEncoder()
    le.fit(desarrll_imp[str(c)])
    desarrll_imp[str(c)]=le.transform(desarrll_imp[str(c)]) 


# #### 3.3. Tratamiento de Outliers

# In[ ]:


# Creamos una funcion para poder visualizar los percentiles
def Cuantiles(lista):
    c = [0,1,5,10,20,30,40,50,60,70,80,90,92.5,95,97.5,99,100]
    matrix = pd.concat([pd.DataFrame(c),pd.DataFrame(np.percentile(lista.dropna(),c))],axis = 1)
    matrix.columns = ["Cuantil","Valor_Cuantil"]
    return(matrix)


# In[17]:


# Analizamos las variables numericas
# Variable
Cuantiles(desarrll_imp["ApplicantIncome"]).transpose()
# Nos hacemos la pregunta, podríamos acotar la variable?


# In[ ]:


## ApplicantIncome
cuantil_1 = np.percentile(desarrll_imp["ApplicantIncome"],1)
cuantil_95 = np.percentile(desarrll_imp["ApplicantIncome"],95)

# Reemplazamos el valor minimo y maximo
desarrll_imp.loc[desarrll_imp["ApplicantIncome"]<cuantil_1,"ApplicantIncome"] = cuantil_1
desarrll_imp.loc[desarrll_imp["ApplicantIncome"]>cuantil_95,"ApplicantIncome"] = cuantil_95


# ### **4. Ingeniería y Selección de Variables**

# #### 4.1. Ingenieria de variables

# In[ ]:


# Ingenieria de datos
#Creamos las variables para el entrenamiento o train
desarrll_imp['TotalIncome']    = desarrll_imp['ApplicantIncome'] + desarrll['CoapplicantIncome']
desarrll_imp['Log_LoanAmount'] = round(np.log(desarrll_imp['LoanAmount']+1),2)
# Existen mas variables a trabajar?


# In[ ]:


# Mas variables!
desarrll_imp['AmountxTerm']    = round(desarrll_imp['LoanAmount']/desarrll_imp['Loan_Amount_Term'],2)
desarrll_imp["Cuota_Ingreso1"] = (1000*desarrll_imp["LoanAmount"]/desarrll_imp["Loan_Amount_Term"])/(desarrll_imp["ApplicantIncome"])
desarrll_imp["Cuota_Ingreso2"] = (1000*desarrll_imp["LoanAmount"]/desarrll_imp["Loan_Amount_Term"])/(desarrll_imp["TotalIncome"])
desarrll_imp["Cuota_Ingreso_Hijo"] = (1000*desarrll_imp["LoanAmount"]/desarrll_imp["Loan_Amount_Term"])/(desarrll_imp["TotalIncome"]/(desarrll_imp["Dependents"]+1))


# In[ ]:





# #### 4.1. Selección de variables

# In[ ]:





# In[ ]:


#############################
# Seleccion por Random Forest
from sklearn.ensemble import RandomForestClassifier                                  # Paso01: Instancio el algoritmo

forest = RandomForestClassifier()                                                    # Paso02: Configuro el algoritmo
forest.fit(desarrll_imp.drop('Loan_Status',axis=1), desarrll_imp.Loan_Status)        # Paso03: Ajuste el algoritmo
importances = forest.feature_importances_                                            # Paso04: Importancia!


# In[17]:


# Seleccion por Random Forest
TablaImportancia = pd.concat([pd.DataFrame({'Driver':list(desarrll_imp.drop('Loan_Status',axis=1).columns)}),
                              pd.DataFrame({'Importancia':list(forest.feature_importances_)})], axis = 1)
ImportanciaVariables = TablaImportancia[['Driver','Importancia']].sort_values('Importancia', ascending = False).reset_index(drop = True)
ImportanciaVariables


# In[ ]:





# In[ ]:


#######################
# Selección por WOESS!
final_iv, IV = data_vars(desarrll_imp,desarrll_imp.Loan_Status)


# In[17]:


# Ordenamos el ordenamiento!
IV.sort_values('IV',ascending=False)


# In[ ]:





# In[18]:


#! pip install boruta


# In[19]:


#############################################
# Seleccion Boruta (Permutaciones de arboles)
from sklearn.ensemble import RandomForestClassifier
from boruta import BorutaPy

rfc = RandomForestClassifier()
boruta_selector = BorutaPy(rfc, n_estimators='auto',perc = 50,alpha = 0.05,verbose=2)

x=desarrll_imp.drop('Loan_Status',axis=1).values
y=desarrll_imp.Loan_Status.values

boruta_selector.fit(x,y)

print("==============BORUTA==============")
print (boruta_selector.n_features_)


# In[ ]:


# Elegimos las variables mas relevantes!


# In[ ]:





# ### **5. Modelamiento de Datos o Creación del Algoritmo de ML**

# #### 5.1. Particion Muestral

# In[ ]:





# In[ ]:


# Creación de la data de train y la data de test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split()


# #### 5.2. Algoritmos Machine Learning

# In[19]:


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train,y_train)


# In[ ]:


# Paso N°04: Predecir con el algoritmo entrenado para validar
y_pred_train=lr.predict(X_train) # Prediccion sobre el train
y_pred_test= lr.predict(X_test) # Prediccion sobre el test


# In[19]:


# Paso N°05: Comparar el valor pronosticado con el valor real

from sklearn import metrics as metrics
# Matriz de confusion
print("Matriz confusion: Train")
cm_train = metrics.confusion_matrix(y_train,y_pred_train)
print(cm_train)

print("Matriz confusion: Test")
cm_test = metrics.confusion_matrix(y_test,y_pred_test)
print(cm_test)

# Accuracy
print("Accuracy: Train")
accuracy_train=metrics.accuracy_score(y_train,y_pred_train)
print(accuracy_train)

print("Accuracy: Test")
accuracy_test=metrics.accuracy_score(y_test,y_pred_test)
print(accuracy_test)

# Precision
print("Precision: Train")
precision_train=metrics.precision_score(y_train,y_pred_train)
print(precision_train)

print("Precision: Test")
precision_test=metrics.precision_score(y_test,y_pred_test)
print(precision_test)

# Recall
print("Recall: Train")
recall_train=metrics.recall_score(y_train,y_pred_train)
print(recall_train)

print("Recall: Test")
recall_test=metrics.recall_score(y_test,y_pred_test)
print(recall_test)


# In[ ]:





# In[ ]:


## Modelos Supervisados : Arbol CART


# In[19]:


# Paso N°01: Llamar un algoritmo predictivos
from sklearn.tree import DecisionTreeClassifier

cart = DecisionTreeClassifier(criterion='entropy',
                              max_depth=3,
                              max_features="sqrt")

cart.fit(X_train, y_train) # Entrenamos el algoritmo


# In[ ]:


# Paso N°04: Predecir con el algoritmo entrenado para validar
y_pred_train=cart.predict(X_train) # Prediccion sobre el train
y_pred_test= cart.predict(X_test) # Prediccion sobre el test


# In[19]:


# Paso N°05: Comparar el valor pronosticado con el valor real

from sklearn import metrics as metrics
# Matriz de confusion
print("Matriz confusion: Train")
cm_train = metrics.confusion_matrix(y_train,y_pred_train)
print(cm_train)

print("Matriz confusion: Test")
cm_test = metrics.confusion_matrix(y_test,y_pred_test)
print(cm_test)

# Accuracy
print("Accuracy: Train")
accuracy_train=metrics.accuracy_score(y_train,y_pred_train)
print(accuracy_train)

print("Accuracy: Test")
accuracy_test=metrics.accuracy_score(y_test,y_pred_test)
print(accuracy_test)

# Precision
print("Precision: Train")
precision_train=metrics.precision_score(y_train,y_pred_train)
print(precision_train)

print("Precision: Test")
precision_test=metrics.precision_score(y_test,y_pred_test)
print(precision_test)

# Recall
print("Recall: Train")
recall_train=metrics.recall_score(y_train,y_pred_train)
print(recall_train)

print("Recall: Test")
recall_test=metrics.recall_score(y_test,y_pred_test)
print(recall_test)


# In[ ]:


## Modelos Supervisados : Random Forest ##
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train) # Entrenando un algoritmo


# In[ ]:


# Paso N°04: Predecir con el algoritmo entrenado para validar
y_pred_train=rf.predict(X_train) # Prediccion sobre el train
y_pred_test= rf.predict(X_test) # Prediccion sobre el test


# In[19]:


# Paso N°05: Comparar el valor pronosticado con el valor real
from sklearn import metrics as metrics
# Matriz de confusion
print("Matriz confusion: Train")
cm_train = metrics.confusion_matrix(y_train,y_pred_train)
print(cm_train)

print("Matriz confusion: Test")
cm_test = metrics.confusion_matrix(y_test,y_pred_test)
print(cm_test)

# Accuracy
print("Accuracy: Train")
accuracy_train=metrics.accuracy_score(y_train,y_pred_train)
print(accuracy_train)

print("Accuracy: Test")
accuracy_test=metrics.accuracy_score(y_test,y_pred_test)
print(accuracy_test)

# Precision
print("Precision: Train")
precision_train=metrics.precision_score(y_train,y_pred_train)
print(precision_train)

print("Precision: Test")
precision_test=metrics.precision_score(y_test,y_pred_test)
print(precision_test)

# Recall
print("Recall: Train")
recall_train=metrics.recall_score(y_train,y_pred_train)
print(recall_train)

print("Recall: Test")
recall_test=metrics.recall_score(y_test,y_pred_test)
print(recall_test)


# In[ ]:





# In[19]:


## Modelos Supervisados : AdaBoost ##
from sklearn.ensemble import AdaBoostClassifier # Paso01: Instancio
AdaBoost=AdaBoostClassifier(learning_rate=0.9, n_estimators=10000) # Paso02: Especifico
AdaBoost.fit(X_train, y_train) # Paso03: Entrenamiento algoritmo


# In[ ]:


# Paso N°04: Predecir con el algoritmo entrenado para validar
y_pred_train=AdaBoost.predict(X_train) # Prediccion sobre el train
y_pred_test= AdaBoost.predict(X_test) # Prediccion sobre el test


# In[19]:


# Paso N°05: Comparar el valor pronosticado con el valor real
from sklearn import metrics as metrics
# Matriz de confusion
print("Matriz confusion: Train")
cm_train = metrics.confusion_matrix(y_train,y_pred_train)
print(cm_train)

print("Matriz confusion: Test")
cm_test = metrics.confusion_matrix(y_test,y_pred_test)
print(cm_test)

# Accuracy
print("Accuracy: Train")
accuracy_train=metrics.accuracy_score(y_train,y_pred_train)
print(accuracy_train)

print("Accuracy: Test")
accuracy_test=metrics.accuracy_score(y_test,y_pred_test)
print(accuracy_test)

# Precision
print("Precision: Train")
precision_train=metrics.precision_score(y_train,y_pred_train)
print(precision_train)

print("Precision: Test")
precision_test=metrics.precision_score(y_test,y_pred_test)
print(precision_test)

# Recall
print("Recall: Train")
recall_train=metrics.recall_score(y_train,y_pred_train)
print(recall_train)

print("Recall: Test")
recall_test=metrics.recall_score(y_test,y_pred_test)
print(recall_test)


# In[ ]:


##################################################
## Implementación de Modelos de Machine Learning
##################################################


# In[ ]:


# Leemos el dataset de implementacion, podria ser una informacion a enivar a campanas
implemt = pd.read_csv("") 


# In[ ]:


# Todo lo realizado en el dataset de entrenamiento del modelo lo debemos replicar en el dataset de scoring
implemt.Credit_History = implemt.Credit_History.astype('str')


# In[ ]:


# Imputamos los valores cualitativos por Moda
implemt.Gender = implemt.Gender.fillna("Male")
implemt.Married = implemt.Married.fillna("Yes")
implemt.Self_Employed = implemt.Self_Employed.fillna("Yes")
implemt.Credit_History = implemt.Credit_History.fillna("1")
implemt.Dependents = implemt.Dependents.fillna("0")


# In[ ]:


# Separamos los features categoricos y los numericos
columnas_categoricas = ["Gender","Married","Education","Self_Employed","Property_Area","Dependents","Credit_History"]
columnas_numericas = ["ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term"]


# In[19]:


# Preprocesamiento con LabelEncoder
from sklearn.preprocessing import LabelEncoder
for c in columnas_categoricas:
    print(str(c))
    le = LabelEncoder()
    le.fit(implemt[str(c)])
    implemt[str(c)]=le.transform(implemt[str(c)]) 


# In[ ]:


# Imputamos los valores cuantitativos por Media o Mediana
for c in columnas_numericas:
    median = implemt[c].median()
    implemt[c].fillna(median, inplace=True)


# In[ ]:


# Ingenieria de datos
#Creamos las mismas variables que utilizamos en el train
implemt['TotalIncome']    = implemt['ApplicantIncome'] + implemt['CoapplicantIncome']
implemt['Log_LoanAmount'] = round(np.log(implemt['LoanAmount']+1),2)


# In[ ]:


implemt['AmountxTerm']    = round(implemt['LoanAmount']/implemt['Loan_Amount_Term'],2)
implemt["Cuota_Ingreso1"] = (1000*implemt["LoanAmount"]/implemt["Loan_Amount_Term"])/(implemt["ApplicantIncome"] +1)
implemt["Cuota_Ingreso2"] = (1000*implemt["LoanAmount"]/implemt["Loan_Amount_Term"])/(implemt["TotalIncome"] +1)
implemt["Cuota_Ingreso_Hijo"] = (1000*implemt["LoanAmount"]/implemt["Loan_Amount_Term"])/(implemt["TotalIncome"]/(implemt["Dependents"]+1))


# In[ ]:


# Una vez que tenemos todas las variables podemos scorear o puntuar los registros
# No olvidemos quitar el ID! 


# In[ ]:


# Predecimos sobre el set de datos de implementacion con el modelo entrenado
y_scoring = lr.predict(df_scoring) # Predecimos sobre nuevos clientes o clientes sin la variable dependiente VD
# Juntamos el ID con la clase
data = np.hstack((implemt['Loan_ID'].values.reshape(-1,1), y_scoring.reshape(-1,1)))
# Le asignamos nombres a las columnas
df_submmit = pd.DataFrame(data, columns=['Loan_ID','Loan_Status'])
# Convertimos al formato solicitado por Analytics Vidhya
df_submmit['Loan_Status']=["Y" if i == 1 else "N" for i in df_submmit['Loan_Status']]
# Exportamos la solucion
df_submmit.to_csv('Sol_Stacking001.csv', index=False)


# In[ ]:


# Listo , objetivo cumplido


# In[ ]:





# In[ ]:


# Anexo
get_ipython().system(' pip install woe')


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


# Fin !!

