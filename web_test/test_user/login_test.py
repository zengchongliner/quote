import time
import unittest
import sys

sys.path.append('D:\\Environment\\.jenkins\\workspace')
from HTMLTestRunner import HTMLTestRunner
from quote.base.operation_browser import OperationBrowser
from quote.base.use_browser import UseBrowser
from quote.util.excel_operation import Excel_Operation
from quote.web_page.user.login_page import LoginPage




class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lg=LoginPage()
        self.ob=OperationBrowser(UseBrowser.driver)
        self.exc_opr=Excel_Operation('../../config/crm.xlsx','登录用例参数')

    def test_all_null(self):
        self.lg.login(self.exc_opr.get_cell(1,2),self.exc_opr.get_cell(1,3))
        self.assertEqual(self.exc_opr.get_cell(1,4),self.lg.alert_text())

    def test_username_null(self):
        self.lg.login(self.exc_opr.get_cell(2,2),self.exc_opr.get_cell(2,3))
        self.assertEqual(self.exc_opr.get_cell(2, 4), self.lg.alert_text())

    def test_password_null(self):
        self.lg.login(self.exc_opr.get_cell(3,2),self.exc_opr.get_cell(3,3))
        self.assertEqual(self.exc_opr.get_cell(3, 4), self.lg.alert_text())

    def test_username_error(self):
        self.lg.login(self.exc_opr.get_cell(4,2),self.exc_opr.get_cell(4,3))
        self.assertEqual(self.exc_opr.get_cell(4, 4), self.lg.alert_text())

    def test_password_error(self):
        self.lg.login(self.exc_opr.get_cell(5,2),self.exc_opr.get_cell(5,3))
        self.assertEqual(self.exc_opr.get_cell(5, 4), self.lg.alert_text())

    def test_all_error(self):
        self.lg.login(self.exc_opr.get_cell(6,2),self.exc_opr.get_cell(6,3))
        self.assertEqual(self.exc_opr.get_cell(6, 4), self.lg.alert_text())

    def test_login_sucess(self):
        self.lg.login(self.exc_opr.get_cell(7,2),self.exc_opr.get_cell(7,3))
        self.assertEqual(self.exc_opr.get_cell(7,4), self.lg.login_sucess_message())

    def tearDown(self) -> None:
        time.sleep(2)
        UseBrowser.quit()

if __name__ == '__main__':

    # unittest.main()
    suite=unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTests(test_case)
    date_now=time.strftime('%y-%m-%d',time.localtime())
    with open('../../report/login_report.html','wb+') as file:
        runner=HTMLTestRunner(stream=file, verbosity=1, title=None, description=None)
        runner.run(suite)