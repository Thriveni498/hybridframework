import time

from selenium.webdriver.common.by import By


class TestAccountRegistration:
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_passord_name = "password"
    btn_click_xpath = "//button[text()='Continue']"
    btn_privacy_xpath = "//input[@name='agree']"
    confirmation_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def test_firstname(self, firstname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(firstname)

    def test_lastname(self, lastname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lastname)

    def test_email(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def test_password(self, password):
        time.sleep(2)
        self.driver.find_element(By.NAME, self.txt_passord_name).send_keys(password)

    def test_privacy(self):
        time.sleep(2)
        self.click=self.driver.find_element(By.XPATH, self.btn_privacy_xpath)
        self.driver.execute_script("arguments[0].click();", self.click)
        time.sleep(5)
        print("before privacy method")
    def test_continue(self):
        time.sleep(2)
        self.continue1=self.driver.find_element(By.XPATH, self.btn_click_xpath)
        self.driver.execute_script("arguments[0].click();", self.continue1)
        time.sleep(5)
        print("before continue method")

    def test_accountsuccessfull(self):
        try:
            return self.driver.find_element(By.XPATH, self.confirmation_xpath).text
        except:
            None
