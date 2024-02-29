import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

from utilities import XLUtil


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\testdata.xlsx"
    lst_status = []

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtil.getRowCount(self.path, 'Sheet1')
        print("no of rows", self.rows)

        for r in range(2, self.rows + 1):
            self.user = XLUtil.readData(self.path, 'Sheet1', r, 1)
            self.passw = XLUtil.readData(self.path, 'Sheet1', r, 2)
            self.lp.set_user_name(self.user)
            self.lp.set_password(self.passw)
            self.lp.click_login()
            act_title = self.driver.title
            if "Dashboard" in act_title:
                self.lst_status.append("pass")
            else:
                self.lst_status.append("fail")

        if 'fail' not in self.lst_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
