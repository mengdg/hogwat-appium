from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWeWork:
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

    def teardown(self):
        self.driver.back()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="消息"]').click()
        self.driver.quit()

    def test_punch_card(self):
        """
        打卡
        :return:
        """
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']"))
        ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']").is_displayed()
        print(ele, type(ele))
        assert ele is True

