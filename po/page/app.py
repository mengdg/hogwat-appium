from appium import webdriver

from po.page.base_page import BasePage
from po.page.main_page import MainPage


class App(BasePage):
    """
    封装启动类操作
    """

    def start(self):
        if self.driver is None:
            caps = dict()
            caps['platformName'] = 'android'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = '.launch.LaunchSplashActivity'
            caps['noReset'] = True
            caps['dontStopAppOnReset'] = True
            caps['skipDeviceInitialization'] = True
            caps['skipServerInstallation'] = True
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            caps['settings[waitForIdleTimeout]'] = 0

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)
