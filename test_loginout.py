import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pubulic import login_driver,drivertest
from pages.shop_page import Shop
from pages.login_page import Login
class Testout:
    def test_out(self,login_driver):
        shop_page=Shop(login_driver)
        shop_page.menu_shop()
        login_page=shop_page.logout_shop()
        login_page.true_url()

        assert login_page.find_button()
        print("登出成功")