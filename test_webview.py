from appium import webdriver
from time import sleep


class TestBrowser:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            # 'platformVersion': '6.0',
            'browserName': 'Browser',
            'noReset': True,
            'deviceName': 'emulator-5554',
            'chromedriverExecutable': '/Users/mengdegong/Desktop/Hogwarts/appium/chromedriver'
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        self.driver.find_element_by_id('index-kw').click()
        self.driver.find_element_by_id('index-kw').send_keys('appium')
        self.driver.find_element_by_id('index-bn').click()
        sleep(5)
