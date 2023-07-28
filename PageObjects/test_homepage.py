import time

from selenium.webdriver.common.by import By


class TestHomepage:
    myaccount_xpath="//span[normalize-space()='My Account']"
    Register_linktext="Register"
    Login_linktext="Login"

    def __init__(self,driver):
        self.driver=driver

    def test_Homepage(self):
        self.driver.find_element(By.XPATH, self.myaccount_xpath).click()
        time.sleep(5)
    def test_register(self):
        self.driver.find_element(By.LINK_TEXT, self.Register_linktext).click()
    def test_login(self):
        self.driver.find_element(By.LINK_TEXT, self.Login_linktext).click()
