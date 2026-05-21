from selenium import webdriver
from selenium.webdriver.common.by import By
from pubulic import login_driver

class Checkout:
    def __init__(self,login_driver):
        self.checkout_driver=login_driver
        self.input_first = (By.ID, "first-name")
        self.input_last = (By.ID, "last-name")
        self.input_email = (By.ID, "postal-code")
        self.click_continue = (By.ID, "continue")
        self.geterror_text=(By.XPATH,"//h3[@data-test='error']")


    def first_name(self,firstname):
        self.checkout_driver.find_element(*self.input_first).send_keys(firstname)
        return self

    def last_name(self,lastname):
        self.checkout_driver.find_element(*self.input_last).send_keys(lastname)
        return self

    def postal_code(self,email):
        self.checkout_driver.find_element(*self.input_email).send_keys(email)
        return self

    def continue_click(self):
        self.checkout_driver.find_element(*self.click_continue).click()
        from pages.continue_page import Continue
        return Continue(self.checkout_driver)

    def error_text(self):
        return self.checkout_driver.find_element(*self.geterror_text).text

