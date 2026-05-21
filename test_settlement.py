import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pubulic import drivertest,login_driver
from selenium.common.exceptions import NoSuchElementException
from pages.shop_page import Shop
from pages.cart_page import Cart
from pages.checkout_page import Checkout
from pages.continue_page import Continue


class TestShopping:
    @pytest.mark.parametrize("firstname,lastname,email",[("1","1","1"),("","1","2"),("2","","3"),("2","3","")])
    def test_sett(self,login_driver,firstname,lastname,email):
        shop_page=Shop(login_driver)
        shop_page.add_cart()
        cart_page=shop_page.click_cart()
        assert "Sauce Labs Backpack" in login_driver.page_source
        print("指定商品存在在购物车")
        cart_page.wait_checkout()
        checkout_page = cart_page.checkout_out()
        checkout_page.first_name(firstname)
        checkout_page.last_name(lastname)
        checkout_page.postal_code(email)
        continue_page = checkout_page.continue_click()

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
                continue_page.finish_find()
            checkout_text=checkout_page.error_text()

            assert error_text[cs] in checkout_text
            print(f"预期无填写{cs}失败登录成功")
            return

        continue_page.click_finish()
        assert "Thank you for your order!" in login_driver.page_source
        print("结算成功")



