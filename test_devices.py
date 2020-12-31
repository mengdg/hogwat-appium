from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions
from time import sleep


class TestDevices:
    def setup(self):
        caps = dict()
        caps['platformName'] = 'android'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.android.settings'
        caps['appActivity'] = '.Settings'
        caps['automationName'] = 'uiautomator2'

        caps['noReset'] = True

        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True

        caps['avd'] = 'Pixel_3_API_30'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_call(self):
        self.driver.make_gsm_call('13366470799', GsmCallActions.CALL)

    def test_msg(self):
        self.driver.send_sms('+86-13366470799', 'hello world!!!')

    def test_network(self):
        self.driver.set_network_connection(6)
        sleep(5)
        self.driver.set_network_connection(2)
        sleep(5)
        self.driver.set_network_connection(4)
        sleep(5)

    def test_screenshot(self):
        self.driver.get_screenshot_as_file('./photos/img.png')
