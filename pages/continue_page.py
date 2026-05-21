from selenium import webdriver
from selenium.webdriver.common.by import By
from pubulic import login_driver

class Continue:
    def __init__(self,login_driver):
        self.continue_driver=login_driver
        self.find_finish=(By.ID,"finish")


    def click_finish(self):
        self.continue_driver.find_element(*self.find_finish).click()

    def finish_find(self):
        self.continue_driver.find_element(*self.find_finish)