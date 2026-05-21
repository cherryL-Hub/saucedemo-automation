from selenium.webdriver.common.by import By
from pubulic import drivertest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Login:
    def __init__(self,drivertest):
        self.drivertest=drivertest
        self.username_input=(By.ID,"user-name")
        self.password_input=(By.ID,"password")
        self.login_button=(By.ID,"login-button")
        self.error_text=(By.XPATH,"//h3[@data-test='error']")
        self.url_true="saucedemo.com"

    def goto(self):
        self.drivertest.get("https://www.saucedemo.com/")
        return self

    def input_username(self,username):
        self.drivertest.find_element(*self.username_input).send_keys(username)
        return self

    def input_password(self,password):
        self.drivertest.find_element(*self.password_input).send_keys(password)
        return self

    def error_get(self):
        return self.drivertest.find_element(*self.error_text).text


    def input_loginbutton(self):
        self.drivertest.find_element(*self.login_button).click()
        from pages.shop_page import Shop
        return Shop(self.drivertest)

    def true_url(self):
        WebDriverWait(self.drivertest,5).until(EC.url_contains(self.url_true))
        return self

    def find_button(self):
        return self.drivertest.find_element(*self.login_button)



