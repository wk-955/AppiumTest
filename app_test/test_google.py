from appium import webdriver
import time
import unittest


class TestGoogle(unittest.TestCase):
    def setUp(self):
        desired_caps = {
              "platformName": "Android",
              "platformVersion": "5.1.1",
              "deviceName": "emulator-5554",
              "appPackage": "com.android.chrome",
              "appActivity": "org.chromium.chrome.browser.ChromeTabbedActivity"
            }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(8)

    def test_getWindows(self):
        time.sleep(2)
        # window = self.driver.get_window_size()
        # print(window)
        # 接受协议
        accept = self.driver.find_element_by_id('com.android.chrome:id/terms_accept')
        accept.click()
        time.sleep(2)

        # 无视默认设置
        useless_define = self.driver.find_element_by_id('com.android.chrome:id/button_primary')
        useless_define.click()
        time.sleep(2)

        # self.driver.find_element_by_id('com.android.chrome:id/search_box_text').send_keys('http://www.baidu.com')
        # self.driver.press_keycode(66)
        # self.driver.find_element_by_id('com.android.chrome:id/url_bar')[1].click()
        # self.driver.press_keycode(66)
        self.driver.tap([(200, 100)])

        self.driver.find_element_by_id('com.android.chrome:id/url_bar').send_keys('http://www.baidu.com')
        self.driver.press_keycode(66)
        time.sleep(5)
        print(self.driver.page_source)

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    TG = TestGoogle()
    TG.test_getWindows()