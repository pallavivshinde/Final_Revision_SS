import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_008_drpdown():
    def test_008_dd(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(10)

        driver.maximize_window()

        driver.get("https://www.careinsurance.com/rhicl/proposalcp/renew/index-care")

        driver.find_element(By.XPATH,'//input[@id="policynumber"]').send_keys("12345678")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@placeholder="DOB"]').click()
        time.sleep(1)

        month = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]'))
        month.select_by_index(11)
        time.sleep(5)

        year = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-year"]'))
        year.select_by_visible_text("1998")
        time.sleep(5)

        driver.find_element(By.XPATH,'//a[@data-date="4"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@placeholder="Contact Number"]').send_keys("1234567890")

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_008_DrpDown.pass.png")

        driver.close()





