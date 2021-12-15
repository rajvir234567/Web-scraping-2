from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome('chromedriver/chromedriver')
browser.get(START_URL)
time.sleep(10)

def scrap_data():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    for i in range(0,457):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        ul_tags = soup.find_all("ul", attrs={"class", "exoplanet"})
        for ul in ul_tags:
            li_tags = ul.find_all("li")

            temp_list = []
            for index, li in enumerate(li_tags):
                if(index == 0):
                    temp_list.append(li.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li.contents[0])
                    except:
                        temp_list.append("")
            
            planet_data.append(temp_list)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    

    with open("scrapp_project.csv", "w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)    
        csvWriter.writerows(planet_data)
scrap_data()