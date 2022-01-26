import pandas as pds

acc = pds.read_csv("/content/ACCOUNTS.csv")
dem = pds.read_csv("/content/DEMOGRAPHICS.csv")
loa = pds.read_csv("/content/LOANS.csv")

# acc

s1 = pds.merge(acc, dem, on = "ID", how = 'outer')
full = pds.merge(s1, loa, on = "ID", how = 'outer')

# full

import numpy as np

#full['SEX'] = pds.Series(full['SEX']).str.replace("F", "1")
#full['SEX'] = pds.Series(full['SEX']).str.replace("M", "0").astype(float)
#full['SEX']


full['CHECKING_BALANCE'] = pds.to_numeric(full['CHECKING_BALANCE'], errors='coerce')
full['EXISTING_SAVINGS'] = pds.to_numeric(full['EXISTING_SAVINGS'], errors='coerce')

mediana = ['AGE', 'PAYMENT_TERM', 'INSTALLMENT_PERCENT']
adicional = [
             'CHECKING_BALANCE'
              , 'EXISTING_SAVINGS'
              , 'EXISTING_CREDITS_COUNT'
              , 'JOB_TYPE'
              , 'DEPENDENTS'
              , 'TELEPHONE'
              , 'FOREING_WORKER'
              , 'EMPLOYMENT_DURATION'
              , 'CURRENT_RESIDENCE_DURATION'
              , 'CREDIT_HISTORY'
              , 'PROPERTY'
              , 'INSTALLMENT_PLANS'
              , 'OTHERS_ON_LOAN'
]
x_drop = ['SEX', 'LOAN_AMOUNT', 'LOAN_PURPOSE']
y = ['ALLOW']

full.fillna(
    value = {
        'CHECKING_BALANCE': 0
        , 'EXISTING_SAVINGS': 0
        , 'EXISTING_CREDITS_COUNT': 0
        , 'JOB_TYPE': 0  #####
        , 'DEPENDENTS': 0
        , 'TELEPHONE': 0
        , 'FOREING_WORKER': "0" 
        , 'EMPLOYMENT_DURATION': 0 
        , 'CURRENT_RESIDENCE_DURATION': 0 
        , 'CREDIT_HISTORY': 'NO_CREDITS'
        , 'PROPERTY': 'UNKNOWN'
        , 'HOUSING': 'FREE'
        , 'INSTALLMENT_PLANS': 'NONE'
        , 'OTHERS_ON_LOAN': 'NONE'
    }
    , inplace = True
)
full[mediana] = full[mediana].fillna(full[mediana].median())
full['FOREIGN_WORKER'].fillna(0, inplace = True)

full.isnull().sum()

full = full.dropna()
full

full.isna().sum()

features = [
  "CHECKING_BALANCE",               # Saldo que posee el cliente en su cuenta corriente
  "PAYMENT_TERM",                   # Cantidad de días que el cvliente posee para pagar el préstamo
  "CREDIT_HISTORY",                 # Situación crediticia pasada del cliente
  "LOAN_PURPOSE",                   # Motivo del préstamo
  "LOAN_AMOUNT",                    # Monto del préstamo
  "EXISTING_SAVINGS",               # Saldo de cuenta de ahorros
  "EMPLOYMENT_DURATION",            # Cuántos años ha permanecido el cliente en su empleo
  "INSTALLMENT_PERCENT",            # Cantidad de cuotas en las que el préstamo debe ser pagado
  "SEX",                            # Sexo del cliente
  "OTHERS_ON_LOAN",                 # Denota la existencia de un garante u otro solicitante del préstamo
  "CURRENT_RESIDENCE_DURATION",     # Años que el cliente ha permanecido en su última residencia
  "PROPERTY",                       # Indica si el cliente posee alguna propiedad a su nombre
  "AGE",                            # Edad del cliente
  "INSTALLMENT_PLANS",              # Plan de financiamiento, que puede ser del banco, externo o ninguno
  "HOUSING",                        # Indica si el cliente posee una casa propia
  "EXISTING_CREDITS_COUNT",         # Número de préstamos que le han sido concedidos al cliente en el pasado
  "JOB_TYPE",                       # Tipo de empleo: 0 - desempleado, 1 - no calificado, 2 - autónomo, 3 - calificado
  "DEPENDENTS",                     # Número de personas con acceso a la cuenta
  "TELEPHONE",                      # Denota si el cliente tiene un número de teléfono registrado
  "FOREIGN_WORKER"                  # Denota si el cliente trabaja en un país fuera del banco
]
target = ['ALLOW']

x =  pds.get_dummies(full[features])
y = full[target]

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB 
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.45, random_state = 23)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


tr_model = DecisionTreeClassifier(max_depth=2)
tr_model.fit(x_train, y_train)

y_pred = tr_model.predict(x_test)

f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

rf_model = RandomForestClassifier(n_estimators = 100, max_depth = 30, random_state = 3)
rf_model.fit(x_train, y_train)

y_pred = rf_model.predict(x_test)
f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

rf_model1 = RandomForestClassifier(n_estimators = 500, max_leaf_nodes = 16, max_depth = 30, n_jobs = -1,  random_state = 3)
rf_model1.fit(x_train, y_train)

y_pred = rf_model1.predict(x_test)
f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

gbc_model = GradientBoostingClassifier()
gbc_model.fit(x_train, y_train)
y_pred = gbc_model.predict(x_test)
f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

gbc_model_t = GradientBoostingClassifier(n_estimators=40, random_state=23)
gbc_model_t.fit(x_train, y_train)
y_pred = gbc_model.predict(x_test)
f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))


nb_model = GaussianNB()
nb_model.fit(x_train, y_train)
y_pred = nb_model.predict(x_test)
f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

lg_model = LogisticRegression()
lg_model.fit(x_train, y_train)
y_pred = lg_model.predict(x_test)
f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

svm_model = SVC(probability=True)
svm_model.fit(x_train, y_train)
y_pred = svm_model.predict(x_test)
f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

sgd_model = SGDClassifier(random_state=3)
sgd_model.fit(x_train, y_train)
y_pred = sgd_model.predict(x_test)

f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

from sklearn.ensemble import BaggingClassifier
bag_clf = BaggingClassifier(
    DecisionTreeClassifier(), n_estimators = 500,
    max_samples = 100, bootstrap = True, n_jobs = -1
)
bag_clf.fit(x_train, y_train)
y_pred = bag_clf.predict(x_test)
f11 = accuracy_score(y_test, y_pred)
f12 = f1_score(y_test, y_pred)

print("acc: {0}\nf1: {1}".format(f11, f12))

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
# Un transformador para remover columnas indeseadas
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, x, y=None):
        return self

    def transform(self, x):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = x.copy()
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        return data.drop(labels=self.columns, axis='columns')

challenge_columns = ['ID', 'CHECKING_BALANCE', 'PAYMENT_TERM', 'CREDIT_HISTORY',
       'LOAN_PURPOSE', 'LOAN_AMOUNT', 'EXISTING_SAVINGS',
       'EMPLOYMENT_DURATION', 'INSTALLMENT_PERCENT', 'SEX', 'OTHERS_ON_LOAN',
       'CURRENT_RESIDENCE_DURATION', 'PROPERTY', 'AGE', 'INSTALLMENT_PLANS',
       'HOUSING', 'EXISTING_CREDITS_COUNT', 'JOB_TYPE', 'DEPENDENTS',
       'TELEPHONE', 'FOREIGN_WORKER', 'ALLOW']

unwanted_columns = list((set(challenge_columns) - set(target)) - set(features)) # Remover todas las colunmas que no son features do nuestro modelo

drop_columns = DropColumns(unwanted_columns)


# Creando un Pipeline, adicionando nuestro transformador seguido de un modelo de árbol de decisión
skl_pipeline = Pipeline(steps=[('drop_columns', drop_columns), ('classification', model)])

skl_pipeline
