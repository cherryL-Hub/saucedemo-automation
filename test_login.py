import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pubulic import drivertest

@pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("locked_out_user","secret_sauce")])
def test_login1(drivertest,username,password):
    drivertest.get("https://www.saucedemo.com/")
    drivertest.find_element(By.ID,"user-name").send_keys(username)
    drivertest.find_element(By.ID,"password").send_keys(password)
    drivertest.find_element(By.XPATH, "//input[@id='login-button']").click()

    if username == "locked_out_user":
        with pytest.raises(TimeoutException):
            WebDriverWait(drivertest,5).until(EC.presence_of_element_located((By.CLASS_NAME,"inventory_item_name ")))
        error_text = drivertest.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert "locked out" in error_text
        print("失败用例测试成功")
        return

    WebDriverWait(drivertest, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name ")))
    assert "Products" in drivertest.page_source
    print("成功用例测试成功")


