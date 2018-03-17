#!/usr/bin/python
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
 
class AutoUITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_ui(self):
        filePath = os.path.abspath('index.html')
        self.driver.get("file://" + filePath);
        firstNameField = self.driver.find_element_by_name("fname");
        lastNameField = self.driver.find_element_by_name("lname");

        firstNameField.send_keys("murat");
        lastNameField.send_keys("oksuzer");

        submitButton = self.driver.find_element(by=By.ID, value="submitButton");
        submitButton.click();

        outputDiv = self.driver.find_element_by_id("outputDiv");
        self.assertEqual(outputDiv.text, 'murat oksuzer');
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()