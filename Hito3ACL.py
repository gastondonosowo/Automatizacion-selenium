from selenium import webdriver
import time

nombre = "El Pepe"
apellido = "Ete Sech"
telefono = "56912345678"
mail = "xofob99898@sartess.com"
contrasena = "AnAshEiXdD_"
driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("https://seguro.marca.com/registro/v3/?view=signup")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="didomi-notice-agree-button"]').click()
time.sleep(4)
pathB = driver.find_element_by_xpath('//*[@id="inputEmailSignup"]')
pathB.send_keys(mail)
time.sleep(3)
pathB = driver.find_element_by_xpath('//*[@id="inputPasswordSignup"]')
pathB.send_keys(contrasena)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="iron-page-signup"]/div[1]/div/form/div/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="iron-page-signup"]/div[1]/div/form/div/div[1]/div[3]/div/div').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="iron-page-signup"]/div[1]/div/form/div/div[1]/div[4]/div/div[1]/div').click()
