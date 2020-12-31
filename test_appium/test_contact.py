from appium import webdriver


class TestContact:
    def setup(self):
        caps = dict()
        caps['platformName'] = 'android'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.WwMainActivity'
        caps['noReset'] = True
        caps['dontStopAppOnReset'] = True
        caps['skipDeviceInitialization'] = True
        caps['skipServerInstallation'] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
