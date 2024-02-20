import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

class Test_010_MouseRightClick():

    def test_010_mouse_rightclick(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(10)

        driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        action = ActionChains(driver)

        right_click = driver.find_element(By.XPATH,"//span[text()='right click me']")
        time.sleep(5)

        action.context_click(right_click).perform()
        time.sleep(5)

        driver.find_element(By.XPATH,"//span[text()='Edit']").click()
        time.sleep(5)

        alert_message = Alert(driver).text
        time.sleep(3)

        print("\n ------- ALERT TEXT------")

        print("\n",alert_message)

        print('\n----------------------')

        Alert(driver).accept()
        time.sleep(5)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_010_rightClick.png")

        driver.quit()









