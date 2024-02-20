import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_007_explicit_wait():
    def test_007_explicitwait(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(10)
        time.sleep(2)

        driver.maximize_window()
        time.sleep(2)

        driver.get("https://www.google.com")
        time.sleep(2)

        driver.find_element(By.XPATH,'//textarea[@title="Search"]').send_keys('Internet Speed Test')
        time.sleep(2)

        driver.find_element(By.XPATH,'(//input[@value="Google Search"])[1]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//div[text()='RUN SPEED TEST']").click()

        try:
            wait = WebDriverWait(driver, 35, poll_frequency=0.5)

            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '(//div[@class="lv7K9c"])[3]')))

            print("\n-----------DOWNLOADED SPEED------------")
            downlaod = driver.find_element(By.XPATH, '(//div[@class="lv7K9c"])[3]').text
            print("\n my downloaded speed is:", downlaod)

            print("----------UPLODED SPEED------------")
            upload = driver.find_element(By.XPATH, '//p[@jsname="dSdcdd"]').text
            print("\n my upload speed is:", upload)

            print("---------YOUR INTERNET SPEED CONNECTION -------")
            message = driver.find_element(By.XPATH, "//p[@class='MGCMLc']").text
            print("\n", message)

            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_007_explicit.pass.png")

            driver.close()
            assert True

        except:
            print('---------------SORRY, SOMETHING WENT WRONG, PLEASE TRY LATER---------------')
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_007_explicit.fail.png")

            assert False
        driver.quit()











