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

with open('test.csv', mode='r') as file:
    reader = csv.reader(file)
    with open('clients.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in reader:
            print(">>> ", row[0])
            driver.get(row[0])
            time.sleep(2)

            # set scroll goes to end
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            match=False
            while(match==False):
                lastCount = lenOfPage
                time.sleep(3)
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                    match=True
            ############################
            # print("the end")
            provider_links = []
            provider_elements = driver.find_elements(By.XPATH, '//*[@id="maincontent"]/div[2]/div/article/a')
            for provider_element in provider_elements:
                provider_link = provider_element.get_attribute("href")
                # print("provider link >>> ", provider_link)
                provider_links.append(provider_link)
            for provider_link in provider_links:
                driver.get(provider_link)
                
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