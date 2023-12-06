import csv
from selenium.webdriver.common.by import By
import time
from seleniumbase import Driver

driver = Driver(uc=True)
pageCount = 1
with open('URL.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("--------------------", pageCount, "---------------------")
        pageCount += 1
        Region = row[0]
        driver.get(row[1])
        time.sleep(2)

        # set scroll goes to end
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(5)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True

        provider_links = []
        provider_elements = driver.find_elements(By.XPATH, '//*[@id="maincontent"]/div[2]/div/article/a')
        for provider_element in provider_elements:
            provider_link = provider_element.get_attribute("href")
            provider_links.append(provider_link)
        for provider_link in provider_links:
            driver.get(provider_link)
            
            try:
                pageTitle = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[1]').text
                name = pageTitle.split("\n")[0]
                title = pageTitle.split("\n")[1]
            except:
                name = "No data"
                title = "No data"

            try:
                Bio = driver.find_element(By.XPATH, '//*[@id="providerProfile"]/div[1]/div/div[2]/div[3]/p').text
            except:
                Bio = "No data"
            
            try:
                specialties = driver.find_elements(By.CSS_SELECTOR, 'div.m_specialties>ul')[0].text
                specialties = specialties.replace("\n", ", ")
            except:
                specialties = "No data"
            try:
                Pay_with_insurance = driver.find_elements(By.CSS_SELECTOR, 'div.m_insurance>ul')[0].text
                Pay_with_insurance = Pay_with_insurance.replace("\n", ", ")
            except:
                Pay_with_insurance = "No data"

            try:
                Accepted_programs = driver.find_elements(By.XPATH, 'div.m_insurance>ul')[1].text
            except:
                Accepted_programs = "No data"

            try:
                Locations = driver.find_elements(By.CSS_SELECTOR, 'div.m_location>ul')[0].text
                Locations = Locations.replace("\n", ", ")
            except:
                Locations = "No data"

            try:
                Pay_out_of_pocket = driver.find_elements(By.CSS_SELECTOR, 'div.m_out-of-pocket>ul>li:first-child>div>span:nth-child(2)>div:nth-child(2)')[0].get_attribute('innerText')
            
                Min_Range = Pay_out_of_pocket.split("-")[0]

                Max_Range = "$" + Pay_out_of_pocket.split("-")[1]
            except:
                Pay_out_of_pocket = "No data"
                Min_Range = "No data"
                Max_Range = "No data"
            try:
                Licensed_in = driver.find_elements(By.CSS_SELECTOR, 'div.category-info-group-wrapper > div:last-child > ul')[0].text
                Licensed_in = Licensed_in.replace("\n", ", ")
            except:
                Licensed_in = "No data"

            headers = ["State USED", "Profile URL", "Name", "Title", "Bio", "Specialties", "Pay with insurance", "Accepted programs", "Pay out of pocket", "Min Range", "Max Range", "Licensed in"]
            results = [Region, provider_link, name, title, Bio, specialties, Pay_with_insurance, Accepted_programs, Pay_out_of_pocket, Min_Range, Max_Range, Licensed_in]
            
            # Open the file in append mode
            with open('clients.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(results)
            print("Write success!!!")
driver.close()    