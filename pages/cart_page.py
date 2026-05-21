from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pubulic import login_driver

class Cart:
    def __init__(self,login_driver):
        self.cart_driver=login_driver
        self.wait_trollyname = (By.CLASS_NAME, "inventory_item_name")
        self.delete_trolly = (By.ID, "remove-sauce-labs-backpack")
        self.back_page = (By.ID, "continue-shopping")
        self.find_checkout=(By.ID,"checkout")
        self.click_checkout=(By.ID,"checkout")
        self.input_first=(By.ID,"first-name")
        self.input_last=(By.ID,"last-name")
        self.input_email=(By.ID,"postal-code")
        self.click_continue=(By.ID,"continue")

    def wait_cart_page(self):
        WebDriverWait(self.cart_driver,5).until(EC.presence_of_element_located(self.wait_trollyname))
        return self

    def remove_cart(self):
        self.cart_driver.find_element(*self.delete_trolly).click()
        return self

    def continue_shopping(self):
        self.cart_driver.find_element(*self.back_page).click()
        from pages.shop_page import Shop
        return Shop(self.cart_driver)

    def wait_checkout(self):
        WebDriverWait(self.cart_driver, 5).until(EC.visibility_of_element_located(self.find_checkout))
        return self

    def checkout_out(self):
        self.cart_driver.find_element(*self.click_checkout).click()
        from pages.checkout_page import Checkout
        return Checkout(self.cart_driver)

