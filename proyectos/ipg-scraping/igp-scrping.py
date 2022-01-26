for i in range(1, 3):
    print(i)

# from lib2to3.pgen2 import driver
# from nbformat import write
# from numpy import append
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# import csv

# driver = webdriver.Firefox(executable_path="geckodriver.exe")

# driver.get("https://www.igp.gob.pe/servicios/centro-sismologico-nacional/ultimo-sismo/sismos-reportados")

# x = []

# for i in range(1, 12):
#     mes = "mes" + str(i)
#     # print(x)
#     x.append(mes)
# print(x)


# for i in x:
#     driver.find_element_by_id(i).click()


# num = Select(driver.find_element_by_name('sismosreportados_length'))
# num.select_by_visible_text("100")

# report = []

# for i in range(1, 55):
#     z = driver.find_element_by_xpath( "/html/body/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[1]").text
#     r = str(z)
#     #print("\n")
#     #print(z)
#     report.append(z)

# with open("report_22_55.csv") as fl:
#     writer = csv.writer(fl)
#     writer.writerows(report)

# "/html/body/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]"
# "/html/body/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[1]"
# "/html/body/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[17]/td[1]"
# driver.find_element_by_xpath("")

# elem = driver.find_element_by_class_name("sorting_1")
# print(elem)



# elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[5]/a[1]")
# href = elem.get_attribute("href")
# print(href)