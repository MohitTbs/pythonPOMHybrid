import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.createlog import LogGen2
from utilities.readProperties import ReadConfig

from pageObjects.TimesheetPage import TimesheetPage

class TestTimesheetModule:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen2.loggen()

    @pytest.mark.sanity
    def test_add_timesheet(self, setup):
        LogGen2.static_logger.info('*********** test_add_timesheet  started **********')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.tp = TimesheetPage(self.driver)
        self.tp.addTimesheet()
        LogGen2.static_logger.info('*********** test_add_timesheet  ended **********')

