from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

delay = 3

d1 = wd.Firefox(executable_path="/home/jhon/Downloads/geckodriver")
d1.get("https://www.resultados.eleccionesgenerales2021.pe/EG2021/EleccionesPresidenciales/RePres/T")


ambito = d1.find_element_by_id("select_ambito")
#ambito = d1.find_element_by_class_name("select_ubigeo ng-untouched ng-pristine ng-valid")

ambito1 = Select(ambito)

opt = ambito1.options

# for i in opt:
#     print(i.text)

ambito1.select_by_index(1)

d1.refresh()

try:
    myElem = WebDriverWait(d1, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

dep = d1.find_element_by_id('select_departamento')

dep1 = Select(dep)


opt_dep = dep1.options

for i in opt_dep:
    # if i != '--TODOS--':
    print(i.text)

dep1.select_by_index(2)

prov = Select(d1.find_element_by_id("cod_prov"))

opt_prov = prov.options

try:
    myElem = WebDriverWait(d1, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

prov.select_by_index(2)

try:
    myElem = WebDriverWait(d1, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

d1.find_element_by_class_name("icon-excel").click()