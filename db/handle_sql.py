import pymysql

from quote.util.excel_operation import Excel_Operation


class Sql_Operation:

    def __init__(self,host,user,password,database,port,charset):
        # 创建连接
        self.conn = pymysql.Connection(host=host, user=user, password=password,
                                       database=database, port=port, charset=charset)
        # 创建游标
        # self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()

        self.exc_sql_opr=Excel_Operation('../config/crm.xlsx','数据库sql')

    # 新增数据
    def insert_operation(self, sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()

    # 查询数据
    def search_operation(self,sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            res=self.cur.fetchall()
        except Exception as e:
            print(e,'search failed')
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()
        return res

    # 更新数据
    def update_operation(self,sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            # 提交
            self.conn.commit()
        except Exception as e:
            print(e,'update failed')
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()

    # 删除数据
    def delete_operation(self,sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            # 提交
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            # 关闭游标
            self.cur.close()
            # 关闭连接
            self.conn.close()

sql_opr=Sql_Operation('172.17.4.242','root','123456','quote',3306,'utf8')
print(sql_opr.search_operation(sql_opr.exc_sql_opr.get_cell(1,1)))
# # sql_opr.delete_operation("delete from customer_info where customer_name='曾崇林'")
# # sql_opr.search_operation("select * from customer_info where customer_name='曾崇林'")
# sql_opr.search_operation(sql_opr.exc_opr.get_cell(0,1))