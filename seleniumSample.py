#!/usr/bin/python
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
  
driver = webdriver.Firefox()
filePath = os.path.abspath('index.html')
print(filePath);
driver.get("file://" + filePath);
firstNameField = driver.find_element_by_name("fname");
lastNameField = driver.find_element_by_name("lname");

firstNameField.send_keys("murat");
lastNameField.send_keys("oksuzer");

submitButton = driver.find_element(by=By.ID, value="submitButton");
submitButton.click();
time.sleep( 5);

outputDiv = driver.find_element_by_id("outputDiv");
print(outputDiv.text)

driver.quit()