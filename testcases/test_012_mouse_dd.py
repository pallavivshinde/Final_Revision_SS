import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Test_mouse_dragdrop():

    def test_012_mouse_dd(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(10)

        driver.get("https://demo.automationtesting.in/Static.html")
        time.sleep(2)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_012_dd_before.png")
        time.sleep(5)

        driver.execute_script("window.scrollBy(0,500)")
        time.sleep(3)

        action= ActionChains(driver)

        src =driver.find_element(By.XPATH,"//img[@id='angular']")

        trg  = driver.find_element(By.XPATH,"//div[@class='dragged']")

        action.drag_and_drop(src,trg).perform()

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_012_dd_after.png")

        driver.close()
