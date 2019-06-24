# -*- coding: utf-8 -*-
"""
@author: Ritesh Rajput | riteshrajput381@gmail.com
This script is used to get info from https://electoralsearch.in/##resultArea  
Website : https://electoralsearch.in/##resultArea
"""

# Libraries
import json
import time
from pytesseract import image_to_string 
from PIL import Image
import pytesseract
from selenium import webdriver
from bs4 import BeautifulSoup as BSoup

def get_captcha_text(location, size):
    
    ''' Edit this path to your stored tesseract.exe path '''
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    im = Image.open('Screenshot.png')
    left = location['x'] + 250
    top = location['y'] + 200
    right = location['x'] + size['width'] + 170
    bottom = location['y'] + size['height'] + 50
    
    # Define crops points
    im = im.crop((left, right, top, bottom))
    im.save('Screenshot.png')
    captcha_text = image_to_string(Image.open('Screenshot.png'))
    print('CAPTCHA:',captcha_text)
    return captcha_text

def login_to_website():
    # Extracting epic_no of the voter from the json file
    with open('Result.json') as f:
        file = json.load(f)
    epic_no = file['Epic No']
    
    url = 'https://electoralsearch.in/##resultArea'
    
    ''' Edit the path as per your chromedriver.exe path '''
    driver = webdriver.Chrome(executable_path = r"C:\Users\Graphene\Documents\chromedriver.exe")
    print('----------Opening browser----------')
    time.sleep(5)
    driver.get(url)
    driver.set_window_size(1120, 550)
    driver.find_element_by_xpath('//*[@id="continue"]').click()

    # Click on the second tab i.e. epic_no of the webpage
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div/ul/li[2]').click() 
    
    # Screenshot the image of screen and determines location of the captcha
    element = driver.find_element_by_xpath('//*[@id="imgCaptchaDiv"]/img')
    location = element.location
    size = element.size        

    # Name of the voter
    user_id = driver.find_element_by_xpath('//*[@id="name"]')
    user_id.clear()
    user_id.send_keys(epic_no)

    # State of the Voter
    password = driver.find_element_by_xpath('//*[@id="epicStateList"]')
    password.send_keys('Maharashtra')

    voter_details = driver.find_elements_by_xpath('//*[@id="resultsTable"]/tbody/tr/td[1]/form/input[22]')

    # Until we obtain the result it will solve the captcha in loop and break when it founds the result 
    while not (voter_details):
        driver.save_Screenshot('Screenshot.png')
        captcha = driver.find_element_by_xpath('//*[@id="txtEpicCaptcha"]')
        captcha_text = get_captcha_text(location, size)
        time.sleep(5)
        captcha.send_keys(captcha_text)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="btnEpicSubmit"]').click()
        time.sleep(7)
        voter_details = driver.find_elements_by_xpath('//*[@id="resultsTable"]/tbody/tr/td[1]/form/input[22]')        
        if voter_details:
            break
        print('----------Captcha not solved, Please wait----------')
    print('----------DONE!!!----------')
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="resultsTable"]/tbody/tr/td[1]/form/input[22]').click
    
    # Parsing the page through BeautifulSoup
    bs_obj = BSoup(driver.page_source, 'html.parser')
    
    # Finding the detials of the Voter
    for i in bs_obj.select('tbody'):
        text = i.get_text()
    cleanedtext = text.strip()
    if cleanedtext: 
        print(cleanedtext)    
    
    # Saving it in a text file
    file = open("FinalText.txt","w", encoding='utf-8') 
    file.write(cleanedtext)
    file.close()
      
login_to_website()