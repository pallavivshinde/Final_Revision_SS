import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Test_009_mouse_hover():
    def test_009_mouse_hover_action(self):

        driver =  webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(10)

        driver.get("https://www.google.com")

        driver.find_element(By.XPATH,'//textarea[@title="Search"]').send_keys("Vtiger")
        time.sleep(5)

        driver.find_element(By.XPATH,'(//input[@value="Google Search"])[1]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,'(//h3[@class="LC20lb MBeuO DKV0Md"])[1]').click()
        time.sleep(3)

        actions = ActionChains(driver)

        resources = driver.find_element(By.XPATH,"//a[contains(text(),'Resources')]")
        time.sleep(3)

        actions.move_to_element(resources).perform()
        time.sleep(3)

        driver.find_element(By.XPATH,"(//a[@class='list-link'][normalize-space()='Contact Us'])[1]").click()
        time.sleep(3)

        text1= driver.find_element(By.XPATH,'(//div[@class="col-12 col-md-4 border-left border-dark mb-4 pl-3 py-2 lift"])[2]').text
        time.sleep(3)

        print("\n*** CONTACT INFO AFTER SUCESSFUL MOUSE HOVER ***")
        print("\n",text1)

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_009_mouseAction.png")

        driver.quit()

