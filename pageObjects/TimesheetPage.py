from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


class TimesheetPage:

    def __init__(self, driver):
        self.driver = driver

    def addTimesheet(self):
        wait_for_loader(self.driver)
        self.driver.find_element(By.XPATH, "//span[@class='sidebar_menu_link' and text()='Timesheet']").click()
        wait_for_loader(self.driver)
        assert "TimeClockWizard" in self.driver.title
        print(self.driver.title)
        time.sleep(2)
        self.driver.find_element(By.ID, "ddlEmployeeList_chosen").click()
        self.driver.find_element(By.XPATH, "//li[text()='All Employees']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='search-block']/a").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "add_task_link_two").click()
        time.sleep(3)
        el2 = self.driver.find_element(By.ID, "ddltmpopupEmployeeList")
        sel = Select(el2)
        sel.select_by_visible_text("Hackshaw")
        sd = self.driver.find_element(By.ID, "txtStartDateClock")
        sd.clear()
        sd.send_keys("21/02/2024")
        st = self.driver.find_element(By.ID, "txtstartTimeClock")
        st.clear()
        st.send_keys("1:15 AM")
        ed = self.driver.find_element(By.ID, "txtEndDateClock")
        ed.clear()
        ed.send_keys("21/02/2024")
        et = self.driver.find_element(By.ID, "txtEndTimeClock")
        et.clear()
        et.send_keys("1:20 AM")
        save_btn = self.driver.find_element(By.ID, "btntimesheetpopupSave")
        loc = self.driver.find_element(By.ID, "ddlLocationClocked")
        el1 = Select(loc)
        el1.select_by_visible_text("India")
        jobs = self.driver.find_element(By.ID, "ddlJobClocked")
        el1 = Select(jobs)
        el1.select_by_visible_text("Home")
        save_btn.click()
        time.sleep(5)
        self.driver.quit()


def wait_for_loader(driver):
    wait = WebDriverWait(driver, 30)
    wait.until(EC.invisibility_of_element(driver.find_element(By.ID, 'divLoading')))
    wait.until(EC.invisibility_of_element(driver.find_element(By.ID, 'divLoading')))
