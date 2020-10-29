import time

from selenium.webdriver.common.alert import Alert

from quote.web_page.user.login_page import LoginPage


class CustomerPage:

    def __init__(self):
        self.lp=LoginPage()
        self.lp.login('admin','123456')

    def customer_add(self,**kwargs):
        # 定位客户的添加按钮
        self.lp.mylog.set_msc('------------------添加开始------------------', 'info')
        self.lp.browser_opr.change_frame(self.lp.yaml_opr.get_locator('FrameName','top'))
        self.lp.browser_opr.click_element(self.lp.yaml_opr.get_locator('TopFrame','cus_message'))
        self.lp.mylog.set_msc('cus_message is sucessful~~~','info')
        self.lp.browser_opr.change_frame(self.lp.yaml_opr.get_locator('FrameName','main'))
        self.lp.browser_opr.click_element(self.lp.yaml_opr.get_locator('MainFrame','add_customer'))
        self.lp.mylog.set_msc('add_customer is sucessful~~~', 'info')
        # 将日期删除只读属性
        self.lp.browser_opr.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        # 添加客户的必要信息
        self.lp.browser_opr.send_keys(self.lp.yaml_opr.get_locator('AddCustomer','customer_name'),
                                      kwargs.get('customer_name'))
        self.lp.mylog.set_msc('customer_name is sucessful~~~','info')
        self.lp.browser_opr.send_keys(self.lp.yaml_opr.get_locator('AddCustomer','postion'),
                                      kwargs.get('postion'))
        self.lp.mylog.set_msc('postion is sucessful~~~', 'info')
        self.lp.browser_opr.send_keys(self.lp.yaml_opr.get_locator('AddCustomer','email'),
                                      kwargs.get('email'))
        self.lp.mylog.set_msc('email is sucessful~~~', 'info')
        self.lp.browser_opr.send_keys(self.lp.yaml_opr.get_locator('AddCustomer','contact'),
                                      kwargs.get('contact'))
        self.lp.mylog.set_msc('contact is sucessful~~~', 'info')
        self.lp.browser_opr.send_keys(self.lp.yaml_opr.get_locator('AddCustomer','birthday_datetime'),
                                      kwargs.get('birthday_datetime'))
        self.lp.mylog.set_msc('birthday_datetime is sucessful~~~', 'info')

        time.sleep(2)
        # 点击添加
        self.lp.browser_opr.click_element(self.lp.yaml_opr.get_locator('AddCustomer','submit'))
        self.lp.mylog.set_msc('submit is sucessful~~~', 'info')

    def customer_update(self):
        pass

    def alert_text(self):
        alert=Alert(self.lp.browser_opr.driver)
        return alert.text
