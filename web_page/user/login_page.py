import time

from selenium.webdriver.common.alert import Alert
from quote.base.operation_browser import OperationBrowser
from quote.base.use_browser import UseBrowser
from quote.config.log_crm import Mylog
from quote.util.yaml_operation import Yaml_Operation


class LoginPage:

    def __init__(self):
        self.browser_use = UseBrowser()
        self.browser_opr = OperationBrowser(UseBrowser.driver)
        self.browser_opr.open_url('http://172.17.4.216:8080/crm')
        self.yaml_opr=Yaml_Operation('../../config/locator.yaml')
        self.mylog=Mylog()

    def login(self,username,password):
        self.mylog.set_msc('------------------登录开始------------------','info')
        self.browser_opr.send_keys(self.yaml_opr.get_locator('LoginPage', 'username'), username)
        self.mylog.set_msc('username is sucessful~~~','info')
        time.sleep(2)
        self.browser_opr.send_keys(self.yaml_opr.get_locator('LoginPage','password'),password)
        self.mylog.set_msc('password is sucessful~~~','info')
        time.sleep(2)
        self.browser_opr.click_element(self.yaml_opr.get_locator('LoginPage','submit'))
        self.mylog.set_msc('submit is sucessful~~~','info')
        time.sleep(2)

    def alert_text(self):
        alert=Alert(self.browser_opr.driver)
        return alert.text

    def login_sucess_message(self):
        self.browser_opr.change_frame(self.yaml_opr.get_locator('FrameName','top'))
        return self.browser_opr.get_text(self.yaml_opr.get_locator('TopFrame','cus_message'))