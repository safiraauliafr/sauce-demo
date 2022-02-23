from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from project.Page.loginPage import LoginPage
from project.Page.homePage import HomePage

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        login = LoginPage(driver)
        login.enter_uname('standard_user')
        login.enter_password('secret_sauce')
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_product()
        homepage.fill_firstName('Safira')
        homepage.fill_lastName('Aulia')
        homepage.fill_zipCode('15125')
        homepage.continue_shopping()

        title = self.driver.find_element_by_class_name('complete-header').text
        assert title in "THANK YOU FOR YOUR ORDER"
        self.driver.implicitly_wait(5)

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

        print('Test Finished')

