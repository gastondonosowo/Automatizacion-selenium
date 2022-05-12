from selenium import webdriver
import time

mail = "catew75673@eoscast.com"
contrasena = "HolaHola1234_"
contrasena_nueva = "HolaHola1234_"

driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("https://familyshop.cl/on/demandware.store/Sites-FamilyShop-Site/es_CL/Login-Show")

time.sleep(3)

pathB = driver.find_element_by_xpath('//*[@id="login-form-email"]')
pathB.send_keys(mail)
pathB = driver.find_element_by_xpath('//*[@id="login-form-password"]')
pathB.send_keys(contrasena)

driver.find_element_by_xpath('//*[@id="login"]/form/button').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[2]/div[1]/a').click()

time.sleep(3)

pathB = driver.find_element_by_xpath('//*[@id="currentPassword"]')
pathB.send_keys(contrasena)
pathB = driver.find_element_by_xpath('//*[@id="newPassword"]')
pathB.send_keys(contrasena_nueva)
pathB = driver.find_element_by_xpath('//*[@id="newPasswordConfirm"]')
pathB.send_keys(contrasena_nueva)
driver.find_element_by_xpath('//*[@id="dwfrm_profile"]/div[4]/div[2]/button').click()