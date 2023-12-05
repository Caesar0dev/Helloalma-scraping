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

driver = Driver(uc=True)

driver.get("https://secure.helloalma.com/providers/liam-lane?ct=UmhvZGUlMjBJc2xhbmQlMkMlMjBVU0E%3D&filterables=dGVsZXRoZXJhcHlfcHJlZmVyZW5jZV9vbmxpbmU%3D&lg=LTcxLjQ3NzQyOTE%3D&lt=NDEuNTgwMDk0NQ%3D%3D&st=Ukk%3D")
time.sleep(2)

title = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[1]').text
print("title >>> ", title)
name = title.split("\n")[0]
print("name >>> ", name) 

title = title.split("\n")[1]
print("title >>> ", title)

Bio = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/p').text
print("Bio >>> ", Bio)

specialties = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/div[2]/div[1]/ul').text
specialties = specialties.replace("\n", ", ")
print("specialties >>> ", specialties)

Pay_with_insurance = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/div[2]/div[2]/ul').text
Pay_with_insurance = Pay_with_insurance.replace("\n", ", ")
print("Pay_with_insurance >>> ", Pay_with_insurance)

Accepted_programs = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/div[2]/div[3]/ul/li').text
print("Accepted_programs >>> ", Accepted_programs)

Locations = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/div[2]/div[5]/ul').text
Locations = Locations.replace("\n", ", ")
print("Locations >>> ", Locations)

Pay_out_of_pocket = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/div[2]/div[4]/ul/li[1]/div/span[2]/div[2]').text
print("Pay_out_of_pocket >>> ", Pay_out_of_pocket)
try:
    Min_Range = Pay_out_of_pocket.split("-")[0]
    print("Min_Range >>> ", Min_Range)

    Max_Range = "$" + Pay_out_of_pocket.split("-")[1]
    print("Max_Range >>> ", Max_Range)
except:
    print("wrong pay out element")

Licensed_in = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/div[2]/div[6]/ul').text
Licensed_in = Licensed_in.replace("\n", ", ")
print("Licensed_in >>> ", Licensed_in)

driver.close()    