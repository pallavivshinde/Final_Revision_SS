import time

from selenium import webdriver

class Test_016_ss():
    def test_016_screenshot(self):

        driver = webdriver.Chrome()
        time.sleep(1)

        driver.implicitly_wait(5)

        driver.maximize_window()
        time.sleep(1)

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)

        if(driver.title=='OrangeHRM'):
            time.sleep(2)

            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_16_ss_pass.png")

            print("\n______________YOU ARE AT RIGHT PAGE_____________________")

            driver.close()
            assert True

        else:
            driver.save_screenshot("C:\\Users\\lenovo\\PycharmProjects\\FINAL_PROJECT\\screenshot\\test_16_ss_fail.png")

            print("\n ____________SORRY, YOU ENTERED A WRONG URL______________")

            driver.close()
            assert False

    def test_016_sum(self):

        a=10
        b=5

        add=a+b

        if(add==15):

            print("\n-----------------ADDITION IS SUCCESSFUL--------------")
            print('RESULT=', add)
            assert True;

        else:
            print('SORRY, ADDITION IS POSSIBLE')
            assert False;
