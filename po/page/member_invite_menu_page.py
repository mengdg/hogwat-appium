from appium.webdriver.common.mobileby import MobileBy

from po.page.base_page import BasePage
from po.page.contact_add import ContactAddPage


class MemberInviteMenuPage(BasePage):
    """
    添加成员 PO
    """

    def add_member_manual(self):
        """
        点击手动添加成员
        :return:
        """
        self.find_and_click(MobileBy.XPATH, '//*[@text="手动输入添加"]')
        return ContactAddPage(self.driver)
