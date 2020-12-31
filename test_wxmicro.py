from appium import webdriver


class TestWXMicro:
    def setup(self):
        caps = dict()
        caps['platformName'] = 'android'
        caps['deviceName'] = 'ce061716e537962d017e'
        caps['appPackage'] = 'com.tencent.mm'
        caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        caps['noReset'] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True

        caps['chromedriverExecutable'] = '/Users/mengdegong/Downloads'
        caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appdrand0'}

        caps['adbPort'] = 5038
        caps[''] = ''

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_wx(self):
        import time
        time.sleep(5)
        pass

    def find_top_window(self, driver=None):
        for window in self.driver.window_handles:
            print(window)
            if ":WISIBLE" in self.driver.title:
                print(self.driver.title)
                return True
            else:
                self.driver.switch_to.window(window)
        return False
