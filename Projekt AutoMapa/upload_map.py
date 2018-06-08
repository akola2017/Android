# -*- coding: utf-8" -*
import os
import unittest
from selenium.webdriver.common.keys import Keys
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestUpload(unittest.TestCase):
    def setUp(self):
        # create a dictionary
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'pl.aqurat.automapa'
        desired_caps['appActivity'] = 'pl.aqurat.automapa.info.SplashScreenActivity'
        # localhost + the port from appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_is_storage(self):
        driver = self.driver
        driver.find_element_by_xpath("//android.widget.TextView[@index='2']").click()
        driver.find_element_by_xpath('//android.widget.TextView[@text="AutoMapa"]').click()
        storage_ok = driver.find_element_by_id('pl.aqurat.automapa:id/device_memory').is_enabled()
        self.assertTrue(storage_ok)

    def test_is_card_memory(self):
        driver = self.driver
        driver.find_element_by_xpath("//android.widget.TextView[@index='2']").click()
        driver.find_element_by_xpath('//android.widget.TextView[@text="AutoMapa"]').click()
        card_ok = driver.find_element_by_id('pl.aqurat.automapa:id/device_sd').is_enabled()
        self.assertTrue(card_ok)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUpload)
    unittest.TextTestRunner(verbosity=2).run(suite)
