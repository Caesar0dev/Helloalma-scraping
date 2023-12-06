import csv
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import pandas as pd
import time
import re
import csv
from datetime import datetime
from datetime import date
from seleniumbase import Driver

url = 'https://secure.helloalma.com/providers/liam-lane/?ct=UmhvZGUlMjBJc2xhbmQlMkMlMjBVU0E%3D&filterables=dGVsZXRoZXJhcHlfcHJlZmVyZW5jZV9vbmxpbmU%3D&lg=LTcxLjQ3NzQyOTE%3D&lt=NDEuNTgwMDk0NQ%3D%3D&st=Ukk%3D'
driver = webdriver.Chrome()
driver.get(url) 
time.sleep(3)
sku = driver.find_elements(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/div[2]/div[4]/ul/li[1]/div/span[2]/div[2]')[0].get_attribute('innerText')
print(sku)
driver.quit()