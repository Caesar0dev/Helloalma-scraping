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
            
            pageTitle = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[1]').text
            print("pageTitle >>> ", pageTitle)
            name = pageTitle.split("\n")[0]
            print("name >>> ", name) 

            title = pageTitle.split("\n")[1]
            print("title >>> ", title)

            try:
                Bio = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/p').text
                print("Bio >>> ", Bio)
            except:
                Bio = "No data"
            
            try:
                specialties = driver.find_elements(By.CSS_SELECTOR, 'div.m_specialties>ul')[0].text
                specialties = specialties.replace("\n", ", ")
                print("specialties >>> ", specialties)
            except:
                specialties = "No data"
            try:
                Pay_with_insurance = driver.find_elements(By.CSS_SELECTOR, 'div.m_insurance>ul')[0].text
                Pay_with_insurance = Pay_with_insurance.replace("\n", ", ")
                print("Pay_with_insurance >>> ", Pay_with_insurance)
            except:
                Pay_with_insurance = "No data"

            try:
                Accepted_programs = driver.find_elements(By.XPATH, 'div.m_insurance>ul')[1].text
                print("Accepted_programs >>> ", Accepted_programs)
            except:
                Accepted_programs = "No data"

            try:
                Locations = driver.find_elements(By.CSS_SELECTOR, 'div.m_location>ul')[0].text
                Locations = Locations.replace("\n", ", ")
                print("Locations >>> ", Locations)
            except:
                Locations = "No data"

            try:
                Pay_out_of_pocket = driver.find_elements(By.CSS_SELECTOR, 'div.m_out-of-pocket>ul>li:first-child>div>span:nth-child(2)>div:nth-child(2)')[0].get_attribute('innerText')
                print("Pay_out_of_pocket >>> ", Pay_out_of_pocket)
            
                Min_Range = Pay_out_of_pocket.split("-")[0]
                print("Min_Range >>> ", Min_Range)

                Max_Range = "$" + Pay_out_of_pocket.split("-")[1]
                print("Max_Range >>> ", Max_Range)
            except:
                Pay_out_of_pocket = "No data"
                Min_Range = "No data"
                Max_Range = "No data"
            try:
                Licensed_in = driver.find_elements(By.CSS_SELECTOR, 'div.category-info-group-wrapper > div:last-child > ul')[0].text
                Licensed_in = Licensed_in.replace("\n", ", ")
                print("Licensed_in >>> ", Licensed_in)
            except:
                Licensed_in = "No data"

            headers = ["Name", "Title", "Bio", "Specialties", "Pay with insurance", "Accepted programs", "Pay out of pocket", "Min Range", "Max Range", "Licensed in"]
            results = [name, title, Bio, specialties, Pay_with_insurance, Accepted_programs, Pay_out_of_pocket, Min_Range, Max_Range, Licensed_in]
            
            # Open the file in append mode
            with open('clients.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(results)
driver.close()    