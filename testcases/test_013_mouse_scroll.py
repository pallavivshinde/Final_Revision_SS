import time

from selenium import webdriver

class Test_013_mousescroll():

    def test_013_scroll(self):

        driver = webdriver.Chrome()

        driver.maximize_window()
        time.sleep(5)

        driver.implicitly_wait(10)
        time.sleep(5)

        driver.get("https://www.bbc.com/")
        time.sleep(5)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_013_before_scroll.png")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,1000)")

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_013_after_scroll.png")
        time.sleep(3)

        driver.close()
