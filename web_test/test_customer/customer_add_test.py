import time
import unittest
import sys

sys.path.append('D:\\Environment\\.jenkins\\workspace')
from HTMLTestRunner import HTMLTestRunner
from quote.base.use_browser import UseBrowser
from quote.util.excel_operation import Excel_Operation
from quote.web_page.customer.customer_page import CustomerPage



class CustomerAdd(unittest.TestCase):

    def setUp(self) -> None:
        self.cp=CustomerPage()
        self.exc_opr=Excel_Operation('../../config/crm.xlsx','添加员工用例参数')
        # self.exc_sql_opr=Excel_Operation('../../config/crm.xlsx','数据库sql')
        # self.sql_opr=Sql_Operation('172.17.4.216','root','123456','crm',3306,'utf8')


    def test_customer_add_sucess(self):
        self.cp.customer_add(customer_name=self.exc_opr.get_cell(1,4),postion=self.exc_opr.get_cell(1,5),
                             email=self.exc_opr.get_cell(1,6),contact=self.exc_opr.get_cell(1,7),
                             birthday_datetime=self.exc_opr.get_cell(1,8))
        self.assertEqual(self.exc_opr.get_cell(1,9),self.cp.alert_text())


    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__ == '__main__':

    # unittest.main()
    suite=unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(CustomerAdd)
    suite.addTests(test_case)
    # date_now=time.strftime('%y-%m-%d',time.localtime())
    with open('../../report/report.html','wb+') as file:
        runner=HTMLTestRunner(stream=file, verbosity=1, title=None, description=None)
        runner.run(suite)