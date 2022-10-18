#settup - zustany stejny

from ast import main
from http import server
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

#import for selenium wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_service = Service(executable_path="selenium/chromedriver.exe")
PATH = "selenium/chromedriver.exe"
driver = webdriver.Chrome(service=driver_service)

driver.get("https://chai.ml/")
print(driver.title)

    #konec settupu

import random
import PyPDF2
import os
os.chdir('/home/nikypiky/repos/python-test/hloupy')

#word generation
verb = (random.choice(open('verbs.txt').read().split()).strip())
noun1 = (random.choice(open('nouns.txt').read().split()).strip()) + ('s')
noun2 = (random.choice(open('nouns.txt').read().split()).strip()) + ('s')
adjective = (random.choice(open('adjectives.txt').read().split()).strip())
punctuation = (random.choice(open('punctuation.txt').read().split()).strip())
preposition = (random.choice(open('prepositions.txt').read().split()).strip())

#sentance generation
sentance = noun1 + ' ' + verb + ' ' + adjective + ' ' + noun2 + punctuation


    #write message
search = driver.find_element(By.XPATH, '//*[@id="chat"]/div/div/div/div[3]/div[3]/div/input')
search.send_keys(sentance)
search.send_keys(Keys.RETURN)



