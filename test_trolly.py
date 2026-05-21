import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pubulic import drivertest,login_driver
from pages.shop_page import Shop
from pages.cart_page import Cart

class Testshop:
    def test_cart(self,login_driver):
        shop_page=Shop(login_driver)
        shop_page.add_cart()
        trolley_text=shop_page.get_cart_text()
        assert "1" == trolley_text
        print("添加商品，购物车响应成功")

        cart_page=shop_page.click_cart()
        cart_page.wait_cart_page()
        cart_page.remove_cart()
        back_shop=cart_page.continue_shopping()


        assert "Products" in login_driver.page_source
        trolley_text = back_shop.get_zerotext()
        assert len(trolley_text) == 0
        print("清空购物车成功")

