# -*- coding: utf-8" -*

import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# SLEEPY_TIME = 1 


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
        def test_notifications(self):
            self.driver.open_notifications(self)
            sleep(5)

        def test_first_notification(self):
            self.driver.open_notifications(self)

            els = self.driver.find_element_by_class_name('android.widget.TextView')

            title = False
            body = False

            for el in els:
                print el
                text = el.text

                if text == "USB debugging connected.":
                    title = True

                elif text == "USB debugging connected.":
                    body == True

            self.assertTrue(title)
            self.assertTrue(body)

        def test_first_notification(self):
            self.driver.open_notifications(self)

            els = self.driver.find_element_by_class_name('android.widget.TextView')

            title = False
            body = False

            for el in els:
                print el
                text = el.text

                if text == "USB debugging connected.":
                    title = True

                elif text == "USB debugging connected.":
                    body == True

            self.assertTrue(title)
            self.assertTrue(body)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Installation)
    unittest.TextTestRunner(verbosity=2).run(suite)
