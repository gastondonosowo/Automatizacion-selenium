from selenium import webdriver
import time

nombre = "Nombre"
apellido = "Apellido"
mail = "livoki8755@bunlets.com"
contrasena = "HolaHola1234_"

driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('https://latiendavichy.com/')

time.sleep(13)

driver.find_element_by_xpath('//*[@id="popupContainer"]/div[1]/img').click()
pathB = driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[5]/form/input[1]')
pathB.send_keys('08001')
driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[5]/form/input[2]').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[4]/div[2]/button').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="_mobile_user_info"]').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="login-form"]/div/a/u').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[1]/div/div/label[3]/span').click()

pathB = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[2]/div/div/input')
pathB.send_keys(nombre)
pathB = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[3]/div/div/input')
pathB.send_keys(apellido)
pathB = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[4]/div/div/input')
pathB.send_keys(mail)
pathB = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[5]/div/div/div/input')
pathB.send_keys(contrasena)
driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[8]/div/div/span/input').click()
driver.find_element_by_xpath('//*[@id="customer-form"]/footer/button').click()