import pytest
import allure
import moment

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()



    def test_logout(self):
        try:
            driver = self.driver
            home_page = HomePage(driver)
            home_page.click_welcome_link()
            home_page.click_logout_link()
            x = driver.title
            assert x == "OrangeHRM1"

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            current_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = test_name+"_"+current_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file(
                'C:/Users/Vladimir/python/AutomationFramework_1/screenshots/' + screenshot_name + '.png')
            raise

        except:
            print("There were exeption")
            current_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = test_name + "_" + current_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file('C:/Users/Vladimir/python/AutomationFramework_1/screenshots/'+screenshot_name+'.png')
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("I am inside finally block")





