import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class test_android(unittest.TestCase):

    def setUp(self):
        desired_caps = {}

        #platforma
        desired_caps['platformName'] = 'Android'

        #wersja platformy
        desired_caps['platformVersion'] = '7.0'

        #nazwa urzadzenia
        desired_caps['deviceName'] = 'Gigaset GS170'
        #mozna wpisac desired_caps['deviceName'] = 'PZLBM7LN9D45594S'
        #mobile browser
        #desired_caps['app'] = 'Chrome'

        #aplikacja do testowania
        desired_caps['app'] = PATH('C:\APPTEST\ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'

        #polaczenie z Appium serwer,
        #self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_form(self):
        #wybieramy przycisk add contact
        el=self.driver.find_element_by_class_name('android.widget.Button')
        el.click()
        sleep(5)
        #name=self.find_element_by_id('contactNameEditText')
        #name.send_keys('Nowak')
        #phone=self.find_element_by_id('contactPhoneEditText')
        #phone.send_keys('+48721390544')
        #email = self.find_element_by_id('contactPhoneEditText')
        #email.send_keys('test@wp.pl')

        #lokalizowanie elementu
        text_fields = self.driver.find_elements_by_class_name('android.widget.EditText')
        text_fields[0].send_keys("Zosia")
        text_fields[1].send_keys("+48713805990")
        text_fields[2].send_keys("test@wp.pl")

        #asercje
        el1 = self.assertEqual('Zosia', text_fields[0].text)
        el2 = self.assertEqual('+48713805990', text_fields[1].text)
        el3 = self.assertEqual('test@wp.pl', text_fields[2].text)

        #zapisujemy
        button = self.driver.find_element_by_class_name("android.widget.Button")
        button.click()







       # self.assertEqual(2, len(products))
   # self.driver = webdriver.Remote('http://localhost:4723', desired_caps)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_android)
    unittest.TextTestRunner(verbosity=2).run(suite)