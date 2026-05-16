import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pubulic import drivertest,login_driver
from selenium.common.exceptions import NoSuchElementException
@pytest.mark.parametrize("firstname,lastname,email",[("1","1","1"),("","1","2"),("2","","3"),("2","3","")])
def test_sett(login_driver,firstname,lastname,email):
    login_driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    login_driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    WebDriverWait(login_driver,5).until(EC.visibility_of_element_located((By.ID,"checkout")))
    assert "Sauce Labs Backpack" in login_driver.page_source
    print("指定商品存在在购物车")
    login_driver.find_element(By.ID,"checkout").click()
    login_driver.find_element(By.ID,"first-name").send_keys(firstname)
    login_driver.find_element(By.ID,"last-name").send_keys(lastname)
    login_driver.find_element(By.ID,"postal-code").send_keys(email)
    login_driver.find_element(By.ID,"continue").click()

    error_text={
        "first-name":"First Name",
        "last-name":"Last Name",
        "email-name":"Postal Code"
    }

    cs=None
    if firstname == "":
        cs="first-name"
    elif lastname == "":
        cs="last-name"
    elif email == "":
        cs="email-name"

    if cs:
        with pytest.raises(NoSuchElementException):
            login_driver.find_element(By.ID,"finish")
        checkout_text=login_driver.find_element(By.XPATH,"//h3[@data-test='error']").text

        assert error_text[cs] in checkout_text
        print(f"预期无填写{cs}失败登录成功")
        return

    login_driver.find_element(By.ID,"finish").click()
    assert "Thank you for your order!" in login_driver.page_source
    print("结算成功")



