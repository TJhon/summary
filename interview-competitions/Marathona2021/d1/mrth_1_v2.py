import pandas as pd
import numpy as np


answer = pd.read_csv("https://raw.githubusercontent.com/maratonadev/desafio-1-2021/main/assets/data/ANSWERS.csv")
acc = pd.read_csv("https://raw.githubusercontent.com/maratonadev/desafio-1-2021/main/assets/data/ACCOUNTS.csv")
dem = pd.read_csv("https://raw.githubusercontent.com/maratonadev/desafio-1-2021/main/assets/data/DEMOGRAPHICS.csv")
loa = pd.read_csv("https://raw.githubusercontent.com/maratonadev/desafio-1-2021/main/assets/data/LOANS.csv")

s1 = pd.merge(acc, dem, on = "ID", how = 'outer')
full = pd.merge(s1, loa, on = "ID", how = 'outer')

# full.head(3)

full['CHECKING_BALANCE'] = pd.to_numeric(full['CHECKING_BALANCE'], errors='coerce')
full['EXISTING_SAVINGS'] = pd.to_numeric(full['EXISTING_SAVINGS'], errors='coerce')
full['FOREIGN_WORKER'].fillna(0, inplace = True)

mediana = ['AGE', 'PAYMENT_TERM', 'INSTALLMENT_PERCENT']
full[mediana] = full[mediana].fillna(full[mediana].median())
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

full = full.dropna()
full
# full.isnull().sum()

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
  #"DEPENDENTS",                     # Número de personas con acceso a la cuenta (inbalanced)
  #"TELEPHONE",                      # Denota si el cliente tiene un número de teléfono registrado(.1%)
  "FOREIGN_WORKER"                  # Denota si el cliente trabaja en un país fuera del banco
]
target = ['ALLOW']

#zero = 0.001
answer['CHECKING_BALANCE'] = pd.to_numeric(answer['CHECKING_BALANCE'], errors='coerce')
answer['EXISTING_SAVINGS'] = pd.to_numeric(answer['EXISTING_SAVINGS'], errors='coerce')
answer['FOREIGN_WORKER'].fillna(0, inplace = True)
answer[mediana] = answer[mediana].fillna(answer[mediana].median())
answer.fillna(
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
answer = answer.dropna()
#answer.isna().sum()

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB 
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import BaggingClassifier

from sklearn.preprocessing import StandardScaler

x = pd.get_dummies(full[features])
y = full[target]
answer_pred = pd.get_dummies(full[features])

rs = 23

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.45, random_state = 23)
# sclr = StandardScaler()
# x_train = sclr.fit_transform(x_train)
# x_test = sclr.fit_transform(x_test)
# answer_pred = sclr.fit_transform(answer_pred)


tr_mdl = DecisionTreeClassifier(max_depth = 2, random_state=rs, min_samples_split=10, min_samples_leaf = 2)
rf_mdl = RandomForestClassifier(n_estimators=500, max_depth=30, random_state=  rs)
rf_mdl1 = RandomForestClassifier(n_estimators=500, max_leaf_nodes = 16, max_depth = 30, n_jobs = -1, random_state=rs)
gb_mdl0 = GradientBoostingClassifier(random_state=12)
gb_mdl1 = GradientBoostingClassifier(n_estimators=100, random_state=rs)
nb_mdl = GaussianNB()
lg_mdl = LogisticRegression()
sv_mdl = SVC(probability=True)
sg_mdl = SGDClassifier(random_state=rs)
bag_clf = BaggingClassifier(
    DecisionTreeClassifier(), n_estimators = 500,
    max_samples = 100, bootstrap = True, n_jobs = -1
)


mmdl = []


for mdl in (tr_mdl, rf_mdl, rf_mdl1, gb_mdl0, gb_mdl1, nb_mdl, lg_mdl, sv_mdl, sg_mdl, bag_clf):
  mdl.fit(x_train, np.ravel(y_train))
  y_pred = mdl.predict(x_test)
  #model = model.append(mdl.__class__.__name__)
  #f1 = f1.append(f1_score(y_test, y_pred))
  print(mdl.__class__.__name__, f1_score(y_test, y_pred))

answer["ALLOW"] = pd.DataFrame(rf_mdl.predict(answer_pred))
# answer.info()

answer.to_csv("out.csv", index = False)
