from selenium import webdriver
import time

mail = "livoki8755@bunlets.com"
contrasena = "HolaHola1234_"
contrasena_nueva = "HolaHola1234_"

driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('https://latiendavichy.com/')

time.sleep(13)

driver.find_element_by_xpath('//*[@id="popupContainer"]/div[1]/img').click()
pathB = driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[5]/form/input[1]')
pathB.send_keys('08001')
driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[5]/form/input[2]').click()
driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[4]/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="_mobile_user_info"]').click()

time.sleep(2)

pathB = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[1]/input')
pathB.send_keys(mail)
pathB = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div[1]/input')
pathB.send_keys(contrasena)
driver.find_element_by_xpath('//*[@id="submit-login"]').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="_mobile_user_info"]').click()
driver.find_element_by_xpath('//*[@id="identity-link"]').click()

pathB = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[5]/div/div/div/input')
pathB.send_keys(contrasena)
pathB = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[6]/div/div/div/input')
pathB.send_keys(contrasena_nueva)
driver.execute_script("document.getElementsByName('psgdpr')[0].checked = true;")
driver.execute_script("document.querySelector('.btn.btn-primary.form-control-submit.save_information').click();")