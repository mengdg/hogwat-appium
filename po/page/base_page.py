from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    封装通用类操作
    """

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, element):
        return self.driver.find_element(by, element)

    def finds(self, by, element):
        return self.driver.find_elements(by, element)

    def find_and_click(self, by, element):
        self.driver.find_element(by, element).click()

    def scroll_find(self, text):
        return self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                                 'scrollable(true).instance(0)).'
                                                                 'scrollIntoView(new UiSelector().'
                                                                 f'text("{text}").instance(0));')

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def find_and_send(self, by, element, text):
        self.find(by, element).send_keys(text)

    def wait_for(self, by, element):
        def wait_ele_for(driver: WebDriver):
            eles = self.finds(by, element)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return result

    # 滚动查找，速度比UiScrollable要快很多
    def swipe_find(self, by, element):
        # 减少隐式等待时长
        self.driver.implicitly_wait(1)

        eles = self.finds(by, element)
        while len(eles) == 0:
            self.driver.swipe(0, 600, 0, 400)
            eles = self.finds(by, element)

        # 恢复隐式等待时长
        self.driver.implicitly_wait(10)
        return eles[0]

    def swipe_find_click(self):
        self.swipe_find().click()
