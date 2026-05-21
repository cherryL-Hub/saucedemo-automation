from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_page import Login
from pubulic import login_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Shop:
    def __init__(self,login_driver):
        self.login_driver=login_driver
        self.wait_shop = (By.CLASS_NAME, "inventory_item_name ")
        self.add_trolly=(By.CSS_SELECTOR,"button.btn_inventory")
        self.get_ttext=(By.XPATH,"//span[@class='shopping_cart_badge']")
        self.shop_cart=(By.CLASS_NAME,"shopping_cart_link")
        self.shop_menu=(By.ID,"react-burger-menu-btn")
        self.shop_logout=(By.ID,"logout_sidebar_link")

    def shop_wait(self):
        WebDriverWait(self.login_driver,5).until(EC.presence_of_element_located(self.wait_shop))


    def add_cart(self):
        self.login_driver.find_element(*self.add_trolly).click()
        return self

    def get_cart_text(self):
        return self.login_driver.find_element(*self.get_ttext).text


    def click_cart(self):
        self.login_driver.find_element(*self.shop_cart).click()
        from pages.cart_page import Cart
        return Cart(self.login_driver)

    def get_zerotext(self):
        return self.login_driver.find_elements(*self.get_ttext)


    def menu_shop(self):
        self.login_driver.find_element(*self.shop_menu).click()
        return self

    def logout_shop(self):
        WebDriverWait(self.login_driver,5).until(EC.element_to_be_clickable(self.shop_logout)).click()
        from pages.login_page import Login
        return Login(self.login_driver)
