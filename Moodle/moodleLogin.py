from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import getpass
PATH = os.getcwd()+"\\chromedriver.exe"

driver=webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
kereberos=input("enter your kerebros id:")
passcode = password = getpass.getpass()


driver.find_element_by_id("username").send_keys(kereberos)
driver.find_element_by_id("password").send_keys(passcode)
textfound=driver.find_element_by_id("login").text
# print(textfound)

numbers=[]
for word in textfound.split():
        if word.isdigit():
            numbers.append(int(word))
for word in textfound.split():
    if word=='add':
       driver.find_element_by_id("valuepkg3").send_keys(numbers[0]+numbers[1])
    elif word=='subtract':
        driver.find_element_by_id("valuepkg3").send_keys(numbers[0]-numbers[1])
    elif word=='first':
        driver.find_element_by_id("valuepkg3").send_keys(numbers[0])
    elif word=='second':
        driver.find_element_by_id("valuepkg3").send_keys(numbers[1])

driver.find_element_by_id("loginbtn").send_keys(Keys.RETURN)