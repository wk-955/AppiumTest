from appium import webdriver
import unittest
import time


class Hy(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1.1',
            'deviceName': '127.0.0.1:5555',
            'appPackage': 'com.duowan.kiwi',
            'appActivity': 'com.duowan.kiwi.simpleactivity.SplashActivity'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(8)

    def test_getWindows(self):
        time.sleep(5)
        windows = self.driver.get_window_size()
        print(windows)



if __name__ == '__main__':
    hy = Hy()
    hy.test_getWindows()