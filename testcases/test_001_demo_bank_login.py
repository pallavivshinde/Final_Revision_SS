import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class Test_001_demo_bank_login():

    def test_001_bank_login(self):

        driver = webdriver.Chrome()
        time.sleep(3)

        driver.maximize_window()
        time.sleep(3)

        driver.implicitly_wait(5)
        time.sleep(3)

        driver.get("https://demo.guru99.com/V4/")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="uid"]').send_keys('mngr546288')

        driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('ArumemE')

        driver.find_element(By.XPATH,'//input[@name="btnLogin"]').click()

        try:
            driver.find_element(By.XPATH,"//title[normalize-space()='Guru99 Bank Manager HomePage']")
            time.sleep(3)

            print("\n ***** Login Is Sucessfull ***** ")

            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_001.pass.png")

            txt1 = driver.find_element(By.XPATH,'//marquee[@class="heading3"]').text
            print(txt1)

            driver.find_element(By.XPATH,"//a[normalize-space()='Log out']").click()
            time.sleep(3)

            Alert(driver).accept()
            time.sleep(2)

            driver.close()
            assert True

        except:
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_001.fail.png")

            print("\n ***** Login Is UnSucessfull ***** ")

            assert False


