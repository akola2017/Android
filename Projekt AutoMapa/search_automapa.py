# -*- coding: utf-8" -*
import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

code = "56-100"
street = "pl. Piastowski"
house = "2"
email = "cos@wp.pl"


class TestSearchAutomapa(unittest.TestCase):
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

    def test_search(self):
        driver = self.driver
        driver.find_element_by_xpath("//android.widget.TextView[@index='2']").click()
        driver.find_element_by_xpath('//android.widget.TextView[@text="AutoMapa"]').click()
        if not driver.find_element_by_xpath('//android.widget.Button[@text="Next"]').is_enabled():
            driver.find_element_by_xpath('//android.widget.Button[@text="Terms of use"]').click()
            driver.find_element_by_xpath('//android.widget.Button[@text="OK"]').click()
        driver.find_element_by_xpath('//android.widget.Button[@text="Next"]').click()
        sleep(10)
        driver.find_element_by_id('pl.aqurat.automapa:id/mail').send_keys(email)
        driver.find_element_by_class_name('android.widget.Button').click()
        driver.find_element_by_id('pl.aqurat.automapa:id/buttonSearch').click()
        driver.find_element_by_id('pl.aqurat.automapa:id/city_search').click()
        driver.find_element_by_id('pl.aqurat.automapa:id/filter_input2').send_keys(code)
        driver.find_element_by_id('pl.aqurat.automapa:id/filterable_first_line').click()
        driver.find_element_by_id("pl.aqurat.automapa:id/filter_input").send_keys(street)
        driver.find_element_by_id('pl.aqurat.automapa:id/filterable_first_line').click()
        driver.find_element_by_id('pl.aqurat.automapa:id/filter_input2').send_keys(house)
        driver.find_element_by_id('pl.aqurat.automapa:id/filterable_first_line_end').click()
        driver.find_element_by_class_name('android.widget.Button').click()
        driver.find_element_by_xpath("//android.widget.Button[@text='Show on the map']").click()
        wynik = driver.find_element_by_xpath("//android.widget.TextView[@text='Plac Piastowski • Wołów • PL']")
        self.assertTrue(wynik)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchAutomapa)
    unittest.TextTestRunner(verbosity=2).run(suite)
