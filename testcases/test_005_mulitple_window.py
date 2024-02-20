import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_005_multiple_window_handle():
    def test_005_handle_multiple_window(self):

        driver= webdriver.Chrome()

        driver.implicitly_wait(10)

        driver.maximize_window()
        time.sleep(2)

        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(2)

        driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
        time.sleep(2)

        allwindow = driver.window_handles
        time.sleep(2)

        driver.switch_to.window(allwindow[1])
        time.sleep(2)
        print("\n --------- TEXT IN CHILD WINDOW ----------")
        text1 = driver.find_element(By.XPATH,"//h3[text()='New Window']").text
        print("\n",text1)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_005_child.png")
        time.sleep(2)

        driver.switch_to.window(allwindow[0])
        print("\n-------- TEXT INN PARENT WINDOW----------")
        text2 =driver.find_element(By.XPATH,"//h3[text()='Opening a new window']").text
        print("\n",text2)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_005_parent.png")
        time.sleep(2)

        driver.quit()



