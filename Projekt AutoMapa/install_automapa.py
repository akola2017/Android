# -*- coding: utf-8" -*
import os
import unittest
from appium import webdriver
#from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test_Installation(unittest.TestCase):
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

        #checking installer
    def test_if_installed(self):
        self.assertTrue(self.driver.is_app_installed('pl.aqurat.automapa'))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Installation)
    unittest.TextTestRunner(verbosity=2).run(suite)
