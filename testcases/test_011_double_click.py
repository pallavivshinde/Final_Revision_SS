import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


class Test_011_doubleclick():
    def test_011_mouse_doubleClick(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(10)

        driver.maximize_window()

        driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        action = ActionChains(driver)

        alert = Alert(driver)

        doubleclick= driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")

        print("\n display satus:", doubleclick.is_displayed())

        print("\n display satus:", doubleclick.is_enabled())

        action.double_click(doubleclick).perform()

        mesg = alert.text

        print("\n",mesg)

        alert.accept()

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_011_doubleclick.png")

        driver.quit()


