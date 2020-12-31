from appium.webdriver.common.mobileby import MobileBy

from po.page.base_page import BasePage


class ContactAddPage(BasePage):
    """
    信息录入页面 PO
    """

    def add_contact(self):
        """
        添加信息
        :return:
        """
        # todo 姓名、性别、手机号
        self.find_and_send(MobileBy.XPATH, '//*[contains(@text, "姓名")]/..//*[@text="必填"]', 'aaaaa')

        self.find_and_click(MobileBy.XPATH, '//*[contains(@text, "性别")]/..//*[@text="男"]')

        self.wait_for(MobileBy.XPATH, '//*[@text="女"]')
        self.find_and_click(MobileBy.XPATH, '//*[@text="女"]')

        self.find_and_send(MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="手机号"]', '13366470799')

        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        return True
