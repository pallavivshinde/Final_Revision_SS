import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class Test_003_add_customer_guru():

    def test_003_new_cust(self):

        driver = webdriver.Chrome()
        time.sleep(3)

        driver.maximize_window()
        time.sleep(3)

        driver.implicitly_wait(10)

        driver.get("https://demo.guru99.com/V4/index.php")
        time.sleep(3)

        driver.find_element(By.NAME,'uid').send_keys('mngr546288')
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('ArumemE')
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="btnLogin"]').click()
        time.sleep(3)

        if(driver.title == 'Guru99 Bank Manager HomePage'):
            driver.save_screenshot('C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_003_add_custmr.pass.png')

            print('\n -------------LOGIN SUCCESSFUL-------------')

            driver.find_element(By.XPATH,'//a[text()="New Customer"]').click()
            time.sleep(3)

            driver.find_element(By.XPATH,"//input[@name='name']").send_keys('pallavi suraj shinde')
            time.sleep(3)

            driver.find_element(By.XPATH,'//input[@value="f"]').click()
            time.sleep(3)

            driver.find_element(By.ID, 'dob').send_keys('24011993')
            time.sleep(3)

            driver.find_element(By.XPATH,'//textarea[@name="addr"]').send_keys('M G Road LBS Palace')
            time.sleep(3)

            driver.find_element(By.XPATH,'//input[@name="city"]').send_keys('pune')
            time.sleep(3)

            driver.find_element(By.XPATH,'//input[@name="state"]').send_keys('maharashtra')
            time.sleep(3)

            driver.find_element(By.XPATH,'//input[@name="pinno"]').send_keys('411000')
            time.sleep(3)

            driver.find_element(By.XPATH,'//input[@name="telephoneno"]').send_keys('9595950000')
            time.sleep(3)

            driver.find_element(By.XPATH,'//input[@name="emailid"]').send_keys('abcprgpr@gmail.com')
            time.sleep(3)

            driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('123123')
            time.sleep(3)

            driver.find_element(By.XPATH,'//input[@name="sub"]').click()
            time.sleep(3)

            print("\n---------CUSTOMER ADDED SUCCESSFULLy--------")

            driver.save_screenshot('C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_003_add_custmr.png')
            time.sleep(3)

            driver.find_element(By.XPATH, '//a[text()="Continue"]').click()
            time.sleep(1)

            driver.find_element(By.XPATH,"//a[text()='Log out']").click()
            time.sleep(3)

            Alert(driver).accept()
            time.sleep(3)

            driver.close()
            assert True


        else:
            driver.save_screenshot('C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_003_add_custmr.fail.png')

            print("----------LOGIN UNSUCESSFULL ------------")

            driver.close()
            assert False












