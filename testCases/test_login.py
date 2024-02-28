import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.error('***********Test_001_Login**********')
        self.logger.debug('***********Verify HomePage Title **********')
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Login":
            assert True
            self.logger.debug('***********test_homePageTitle passed **********')
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.logger.debug('***********test_homePageTitle failed **********')
            assert False
        self.driver.close()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        assert "Dashboard" in act_title, "Title did not match"
        self.logger.debug('***********test_login passed **********')
