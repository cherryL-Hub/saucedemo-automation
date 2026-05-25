
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pubulic import drivertest
from pages.login_page import Login

class Testlogin:
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("locked_out_user","secret_sauce")])

    def test_login1(self,drivertest,username,password):
        login_page=Login(drivertest)
        login_page.goto()
        login_page.input_username(username)
        login_page.input_password(password)
        shop_page=login_page.input_loginbutton()


        if username == "locked_out_user":
            with pytest.raises(TimeoutException):
                shop_page.shop_wait()

            error_text=login_page.error_get()
            assert "locked out" in error_text
            print("失败用例测试成功")
            return

        shop_page.shop_wait()
        assert "products" in drivertest.page_source
        print("成功用例测试成功")


