from quote.db.handle_sql import Sql_Operation


class Customer_Operation:

    def __init__(self):
        self.db_opr=Sql_Operation()

    def delete_customer(self):
        self.db_opr.delete_operation('...')