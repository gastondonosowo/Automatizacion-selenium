from selenium import webdriver
import time

mail = "livoki8755@bunlets.com"
contrasena_nueva = "HolaHola1234_"

driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("https://latiendavichy.com/recuperacion-contrasena")

time.sleep(13)

driver.find_element_by_xpath('//*[@id="popupContainer"]/div[1]/img').click()
pathB = driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[5]/form/input[1]')
pathB.send_keys('08001')
driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[5]/form/input[2]').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[4]/div[2]/button').click()

time.sleep(3)

pathB = driver.find_element_by_xpath('//*[@id="email"]')
pathB.send_keys(mail)
driver.find_element_by_xpath('//*[@id="content"]/form/section/div/button[1]').click()

time.sleep(30)

pathB = driver.find_element_by_xpath('//*[@id="content"]/form/section/div[2]/div[1]/div/input')
pathB.send_keys(contrasena_nueva)
pathB = driver.find_element_by_xpath('//*[@id="content"]/form/section/div[2]/div[2]/div/input')
pathB.send_keys(contrasena_nueva)
driver.find_element_by_xpath('//*[@id="content"]/form/section/div[2]/div[3]/div/button').click()


