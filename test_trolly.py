import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pubulic import drivertest,login_driver

def test_cart(login_driver):
    login_driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
    trolley_text=login_driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").text
    assert "1" == trolley_text
    print("添加商品，购物车响应成功")

    login_driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    WebDriverWait(login_driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"inventory_item_name")))
    login_driver.find_element(By.ID,"remove-sauce-labs-backpack").click()
    login_driver.find_element(By.ID,"continue-shopping").click()
    assert "Products" in login_driver.page_source
    trolley_text = login_driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert len(trolley_text) == 0
    print("清空购物车成功")

