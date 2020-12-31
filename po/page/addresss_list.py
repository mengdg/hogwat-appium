from appium.webdriver.common.mobileby import MobileBy

from po.page.base_page import BasePage
from po.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    """
    通讯录列表PO
    """

    def click_add_member(self):
        """
        通讯录
        :return:
        """
        self.scroll_find_click('添加成员')
        return MemberInviteMenuPage(self.driver)
