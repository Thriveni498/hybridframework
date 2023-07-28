import os

from PageObjects.test_homepage import TestHomepage
from PageObjects.AccountRegistrationpage import TestAccountRegistration
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Registartion:
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    def test_Registration(self,setup):
        self.logger.info("*** test_regeistration started***")
        self.driver=setup

        self.driver.get(self.baseURL)
        self.logger.info("*****launching browser**********")
        self.driver.maximize_window()
        self.hp=TestHomepage(self.driver)
        self.hp.test_Homepage()
        self.hp.test_register()

        self.ar=TestAccountRegistration(self.driver)
        self.logger.info("***Registration started***")
        self.ar.test_firstname("Anvi")
        self.ar.test_lastname("Reddi")
        #self.email=randomString.random_string_generator()+'@gmail.com'
        self.ar.test_email("thriveniveeramreddi2022@gmail.com")
        self.ar.test_password("Anvi@2023")
        self.ar.test_privacy()
        self.logger.info("*********privacy polycy******")
        self.ar.test_continue()
        self.logger.info("************ continue button********")
        self.config=self.ar.test_accountsuccessfull()
        if self.config=="Your Account Has Been Created!":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_automation.png")
            self.driver.close()
            assert False

