from selenium import webdriver
import time

mail = "catew75673@eoscast.com"
contrasena_nueva = "HolaHola1234_"

driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("https://familyshop.cl/on/demandware.store/Sites-FamilyShop-Site/es_CL/Login-Show")

time.sleep(3)

driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/div[2]').click()

time.sleep(3)

pathB = driver.find_element_by_xpath('//*[@id="reset-password-email"]')
pathB.send_keys(mail)
driver.find_element_by_xpath('//*[@id="submitEmailButton"]').click()

time.sleep(20)

pathB = driver.find_element_by_xpath('//*[@id="newPassword"]')
pathB.send_keys(contrasena_nueva)
pathB = driver.find_element_by_xpath('//*[@id="newPasswordConfirm"]')
pathB.send_keys(contrasena_nueva)
driver.execute_script("document.querySelector('.btn.btn-save.btn-block.btn-primary').click();")