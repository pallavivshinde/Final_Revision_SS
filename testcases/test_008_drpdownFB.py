import  time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_008_drp_down_FB():
    def test_008_DrpDownFB(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(10)

        driver.maximize_window()

        driver.get("https://www.facebook.com")

        driver.find_element(By.XPATH,'//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys('raha')
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys('kappoor')
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="reg_email__"]').send_keys("abc@gmail.com")
        time.sleep(3)

        driver.find_element(By.XPATH,'//input[@name="reg_passwd__"]').send_keys("12345")
        time.sleep(3)

        date = Select(driver.find_element(By.XPATH,'//select[@name="birthday_day"]'))
        date.select_by_value('11')
        time.sleep(3)

        month=Select(driver.find_element(By.XPATH,'//select[@id="month"]'))
        month.select_by_index(10)
        time.sleep(3)

        year = Select(driver.find_element(By.XPATH,'//select[@id="year"]'))
        year.select_by_visible_text("2011")
        time.sleep(3)

        female_click=driver.find_element(By.XPATH,'(//input[@type="radio"])[1]')
        female_click.click()
        print("\n",female_click.is_selected())

        driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_008_drpdownFB.png")

        driver.quit()





