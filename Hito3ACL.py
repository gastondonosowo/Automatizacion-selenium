from selenium import webdriver
import time

nombre = "NombrE"
apellido = "Apellido"
telefono = "56912345678"
mail = "catew75673@eoscast.com"
contrasena = "HolaHola1234_"

driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("https://familyshop.cl/on/demandware.store/Sites-FamilyShop-Site/es_CL/Login-Show")

time.sleep(2)

driver.find_element_by_xpath('//*[@id="register-tab"]').click()
pathB = driver.find_element_by_xpath('//*[@id="registration-form-fname"]')
pathB.send_keys(nombre)
pathB = driver.find_element_by_xpath('//*[@id="registration-form-lname"]')
pathB.send_keys(apellido)
pathB = driver.find_element_by_xpath('//*[@id="registration-form-phone"]')
pathB.send_keys(telefono)
pathB = driver.find_element_by_xpath('//*[@id="registration-form-email"]')
pathB.send_keys(mail)
pathB = driver.find_element_by_xpath('//*[@id="registration-form-email-confirm"]')
pathB.send_keys(mail)
pathB = driver.find_element_by_xpath('//*[@id="registration-form-password"]')
pathB.send_keys(contrasena)
pathB = driver.find_element_by_xpath('//*[@id="registration-form-password-confirm"]')
pathB.send_keys(contrasena)
driver.find_element_by_xpath('//*[@id="register"]/form/button').click()