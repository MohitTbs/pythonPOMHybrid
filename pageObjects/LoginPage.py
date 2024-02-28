import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    username_box_id = "UserName"
    pass_box_id = "Password"
    login_btn_xpath = "//button[@value='LogIn']"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        self.driver.find_element(By.ID, self.username_box_id).send_keys(username)

    def set_password(self, password):
        time.sleep(3)
        self.driver.find_element(By.ID, self.pass_box_id).send_keys(password)

    def click_login(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
