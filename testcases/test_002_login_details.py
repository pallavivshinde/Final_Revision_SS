from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

class Test_002_demo_guru_details:
    def test_002_details(self):

        driver =  webdriver.Chrome()
        time.sleep(1)

        driver.implicitly_wait(10)
        time.sleep(1)

        driver.maximize_window()
        time.sleep(1)

        driver.get("https://demo.guru99.com/V4/")

        driver.find_element(By.XPATH,'//input[@name="uid"]').send_keys('mngr546288')

        driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('ArumemE')

        driver.find_element(By.XPATH,'//input[@name="btnLogin"]').click()

        if(driver.title=='Guru99 Bank Manager HomePage'):
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_002_login_details.pass.png")
            time.sleep(3)

            print("----------LOGIN SUCESSFULL ------------")

            mesg =driver.find_element(By.XPATH,'//td[@style="color: green"]').text
            print('\n ---------DETAILS ------------')
            print("\n",mesg)
            print('\n------------------------------')

            driver.find_element(By.XPATH,'//a[text()="Log out"]').click()
            time.sleep(3)

            Alert(driver).accept()
            driver.close()
            assert True

        else:
            driver.save_screenshot(
                "C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_002_login_details.fail.png")

            print("----------LOGIN UNSUCESSFULL ------------")

            driver.close()
            assert False








