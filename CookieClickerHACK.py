import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import keyboard

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

const = driver.find_element("xpath", "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")

const.click()
time.sleep(1)

got_it = driver.find_element("xpath", "/html/body/div[1]/div/a[1]")
got_it.click()
time.sleep(1)

eng = driver.find_element("xpath", '//*[@id="langSelect-PL"]')
eng.click()
time.sleep(5)

privacy = driver.find_element("xpath", "/html/body/div[2]/div/ins/img[3]")
privacy.click()
time.sleep(1)

cookie = driver.find_element("xpath", '//*[@id="bigCookie"]')
sklep_products = driver.find_elements("xpath", '/html/body/div/div[2]/div[19]/div[3]/div[6]/*')
sklep_products.reverse()

clicks = 0
enable_click = True

def buy_upgrade():
    ulepszenie = driver.find_elements("xpath", "/html/body/div/div[2]/div[19]/div[3]/div[5]/*")
    ulepszenie.reverse()
    buy_more = False
    for item in ulepszenie:
        if item.get_attribute("class") == "crate upgrade enabled":
            item.click()
            buy_more = True
            break

def buy_item():
    buy_more = False
    for item in sklep_products:
        if item.get_attribute("class") == "product unlocked enabled":
            item.click()
            buy_more = True
            break
    if buy_more is True:
        buy_item()

while 1:
    if enable_click:
        cookie.click()
        clicks += 1
        if clicks == 100:
            buy_upgrade()
            buy_item()
            clicks = 0
    if keyboard.is_pressed('q'):
        enable_click = False
        print("Funkcja zatrzymana")
        time.sleep(1)
    if keyboard.is_pressed('e'):
        enable_click = True
        print("Funkcja wznowiona")
        time.sleep(1)

