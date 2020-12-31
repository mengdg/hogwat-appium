from appium.webdriver.common.mobileby import MobileBy

from po.page.addresss_list import AddressListPage
from po.page.base_page import BasePage


class MainPage(BasePage):
    """
    首页PO
    """

    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/elq" and @text="通讯录"]')
        return AddressListPage(self.driver)
