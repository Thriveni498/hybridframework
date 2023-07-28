import os

from PageObjects.test_homepage import TestHomepage
from PageObjects.test_login import TestLogin
from PageObjects.AccountRegistrationpage import TestAccountRegistration
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    def test_login1(self,setup):
        self.logger.info("*** test_login started***")
        self.driver=setup

        self.driver.get(self.baseURL)
        self.logger.info("*****launching browser**********")
        self.driver.maximize_window()
        self.hp=TestHomepage(self.driver)
        self.hp.test_Homepage()
        self.hp.test_login()

        self.ar=TestLogin(self.driver)
        self.ar.test_inputemail("thriveni498gmail.com")
        self.ar.test_inputpassword("Thri@333")
        self.ar.test_inputlogin()
        if self.driver.title=="My Account":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_automation.png")
            self.driver.close()
            assert False


