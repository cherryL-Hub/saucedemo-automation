import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pubulic import login_driver,drivertest
def test_out(login_driver):
    login_driver.find_element(By.ID,"react-burger-menu-btn").click()
    WebDriverWait(login_driver,5).until(EC.element_to_be_clickable((By.ID,"logout_sidebar_link"))).click()
    WebDriverWait(login_driver,5).until(EC.url_contains("saucedemo.com"))
    assert login_driver.find_element(By.ID,"login-button")
    print("登出成功")