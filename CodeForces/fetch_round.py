from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
PATH = os.getcwd()+"\\chromedriver.exe"

driver=webdriver.Chrome(PATH)

contest = sys.argv[1]
driver.get("https://codeforces.com/contest/"+contest)
problems=len(driver.find_elements_by_xpath("//table[@class='problems']/tbody/tr"))
print(problems)
for r in range(2,problems+1):
    driver.get("https://codeforces.com/contest/"+contest+"/problem/"+chr(65+r-2))
    time.sleep(2)
    os.makedirs(contest+"/"+chr(65+r-2))
    driver.save_screenshot(contest+"/"+chr(65+r-2)+"/problem.png")
    inputs = driver.find_elements_by_class_name("input")
    outputs = driver.find_elements_by_class_name("output")
    for j in range(len(inputs)):
        input_text = inputs[j].find_element_by_tag_name("pre")
        txt = input_text.text
        f = open(contest + "/" + chr(65+r-2) + "/input" + str(j+1) + ".txt", "w")
        f.write(txt)
        f.close
    for j in range(len(outputs)):
        output_text = outputs[j].find_element_by_tag_name("pre")
        txt = output_text.text
        f = open(contest + "/" + chr(65+r-2) + "/output" + str(j+1) + ".txt", "w")
        f.write(txt)
        f.close
driver.quit()