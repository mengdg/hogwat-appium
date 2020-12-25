from appium import webdriver
import pytest
import time
from hamcrest import *

from appium.webdriver.common.touch_action import TouchAction


class TestXueQiuDemo:

    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".common.MainActivity"
        caps["noReset"] = True
        caps['dontStopAppOnReset'] = True
        caps['skipDeviceInitialization'] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()
        self.driver.quit()

    def test_search(self):
        """
        1.打开雪球APP
        2.判断输入框是否可用，并查看搜索框name属性值
        3.打印搜索框这个元素的左上角坐标和他的宽高
        4.点击搜索框
        5.输入框输入"阿里巴巴"
        6.判断【阿里巴巴】是否可见
        如果可见打印"搜索成功"，如果不可见，打印"搜索失败"
        :return:
        """
        search_element = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        if search_element.is_enabled():
            print('搜索框可用')
            print('搜索框的name属性：', search_element.get_attribute('name'))
            print('搜索框宽高', search_element.size)
            self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
            time.sleep(5)
            ele = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").is_displayed()
            print(ele, type(ele))
            if ele:
                print('搜索成功')
            else:
                print('搜索失败')
        else:
            print('搜索框不可用')

    def test_touch_action(self):
        rect = self.driver.get_window_rect()
        width = rect['width']
        height = rect['height']
        x = int(width / 2)
        y = int(height * 4 / 5)
        y_to = int(height * 1 / 5)
        action = TouchAction(self.driver)
        action.press(x=x, y=y).wait(200)
        action.move_to(x=x, y=y_to)
        action.release()
        action.perform()
        time.sleep(3)

    @pytest.mark.parametrize("searchkey,type,expect_price", [
        ('alibaba', 'BABA', 180),
        ('xiaomi', '01810', 10)
    ])
    def test_get_price(self, searchkey, type, expect_price):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys(f'{searchkey}')
        self.driver.find_element_by_xpath(f"//*[@resource-id='com.xueqiu.android:id/name']").click()
        current_price = self.driver.find_element_by_xpath(
            f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert_that(expect_price, close_to(expect_price, expect_price*0.1))

    def test_my_info(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("我的").resourceId("com.xueqiu.android:id/tab_name")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("密码登录")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('mengdegong')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123123')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).scrollIntoView(new UiSelector().'
                                                        'text("顿牛").instance(0));').click()
        time.sleep(3)


if __name__ == '__main__':
    pytest.main()
