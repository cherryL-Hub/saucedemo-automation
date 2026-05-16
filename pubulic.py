import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def drivertest():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture()
def login_driver(drivertest):
    drivertest.get("https://www.saucedemo.com/")
    drivertest.find_element(By.ID,"user-name").send_keys("standard_user")
    drivertest.find_element(By.ID,"password").send_keys("secret_sauce")
    drivertest.find_element(By.XPATH, "//input[@id='login-button']").click()
    WebDriverWait(drivertest,5).until(EC.presence_of_element_located((By.CLASS_NAME,"inventory_item_name")))
    return drivertest


