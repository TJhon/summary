from http import server
from lib2to3.pgen2 import driver
from re import I, search
from nbformat import write
from numpy import append
import numpy as np
import pandas as pd
from selenium import webdriver
import csv
import time

last =  "IGP/CENSIS/RS 2022-0082"

anio, last_report = last[14:18], int(last[19:])

driver = webdriver.Firefox(executable_path="geckodriver.exe")

search = driver.find_element_by_xpath

mag, date, lat, lon, profu, inte = [], [], [], [], [], []

for i in range(1, last_report + 1):
    cero = 4 - len(str(i))
    cero = anio + "-" + cero * "0" + str(i)
    direction = "https://www.igp.gob.pe/servicios/centro-sismologico-nacional/evento/"
    direction1 = direction + cero
    print(direction1)

    driver.get(direction1)
    time.sleep(1)
    mag.append(search('/html/body/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/strong').text)
    date.append(search('/html/body/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/p[1]/span').text)
    lat.append(search('//*[@id="data-latitud"]').text)
    lon.append(search('//*[@id="data-longitud"]').text)
    profu.append(search('/html/body/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/p[1]/span').text)
    inte.append(search("/html/body/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/p[2]/span").text)
    time.sleep(1)    

igp_data = [mag, date, lat, lon, profu]
np_array = np.array(igp_data)

df = pd.DataFrame(data=np_array).T
df.columns = ['M', 'date', 'lat', 'lon', 'prof']

df.to_csv("data/igp_2022.csv", index=False)

print(df)

# with open("igp.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(igp_data)