import time

from selenium.webdriver.common.by import By

class TestLogin:

    txt_email_xpath="//input[@id='input-email']"
    txt_password_xpath="//input[@id='input-password']"
    btn_login_xpath="//button[normalize-space()='Login']"

    def __init__(self,driver):
        self.driver=driver
    def test_inputemail(self,email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def test_inputpassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def test_inputlogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()