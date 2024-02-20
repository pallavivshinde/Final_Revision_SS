import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_006_implicitwait():
    def test_006_implicit_wait_demo(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.implicitly_wait(10)

        driver.maximize_window()

        driver.get("https://www.google.com")

        driver.find_element(By.XPATH,'//textarea[@jsaction="paste:puy29d;"]').send_keys("Internet Speed Test")

        driver.find_element(By.XPATH,'(//input[@value="Google Search"])[1]').click()
        time.sleep(5)

        driver.find_element(By.XPATH,"//div[text()='RUN SPEED TEST']").click()
        time.sleep(25)

        print("\n --------------DOWNLOAD SPEED--------------")
        download = driver.find_element(By.XPATH,'//p[@jsname="Lk0VKd"]').text
        print("\n my downladed speed is:",download)

        print("\n --------------UPLOAD SPEED--------------")
        upload=driver.find_element(By.XPATH,'//p[@jsname="dSdcdd"]').text
        print("\n my uploaded speed is:",upload)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_006_implicit.png")
        time.sleep(5)
        driver.close()





