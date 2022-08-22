from lib2to3.pgen2 import driver
from xml.dom.minidom import Element
from tests import *
from selenium import webdriver

import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


app_url = 'http://127.0.0.1:5000'

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

#station ID to be referenced from an input file.
stn = 'Station_097' 

driver = webdriver.Chrome(PATH)


newpage = driver.get(app_url)

time.sleep(3)
title = driver.title

if (title != 'Assessment Record'):
    print ('Bug - Title doesnot match the requirement.')
else:

    #source = driver.page_source
    nav_station = driver.find_element(By.LINK_TEXT,'Station')
    nav_station.click()

    try:
        stn_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "stationId"))
        )
        stn_element = driver.find_element(By.ID,'stationId')
        stn_element.send_keys(stn)

        stn_element = driver.find_element(By.ID,'target')
        stn_element.send_keys("85") 

        #find the element by X-PATH
        submit_button = driver.find_element(By.XPATH,'/html/body/div[2]/form/button').click()
            

        time.sleep(5)

    
        nav_element = driver.find_element(By.LINK_TEXT,'Assessment Record').click()

        time.sleep(2)

        rec_element = driver.find_element(By.ID,'stationId')
        rec_element.send_keys(stn)

        rec_element = driver.find_element(By.ID,'date')
        rec_element.send_keys("03/03/2022")

        rec_element = driver.find_element(By.ID,'target')
        rec_element.send_keys("85")

        rec_element = driver.find_element(By.ID,'actual')
        rec_element.send_keys("95")



        submit_button = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/form/button')
        submit_button.click()

        time.sleep(5)

        #//*[@id="developers"] - shorter X Path
        nav_station = driver.find_element(By.XPATH,'//*[@id="developers"]')
        nav_station.click()

        time.sleep(5)
           
    finally:
        driver.quit()
