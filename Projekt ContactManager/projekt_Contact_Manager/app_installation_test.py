# -*- coding: utf-8" -*

import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# SLEEPY_TIME = 1 (gdy emulator wolno działa)


class Test_Installation(unittest.TestCase):

    def setUp(self):
        # create a dictionary
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        # first create the APPTEST folder
        desired_caps['app'] = PATH('C:\APPTEST\ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        # localhost + the port from appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def tearDown(self):
            self.driver.quit()

        # checking if the app is installed
        def test_if_installed(self):
            self.assertTrue(self.driver.is_app_installed('io.appium.android.apis'))

        # checking if the app is installed
        def test_if_not_installed(self):
            self.assertFalse(self.driver.is_app_installed('io.appium.android.apis'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Installation)
    unittest.TextTestRunner(verbosity=2).run(suite)
