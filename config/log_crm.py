import logging
import time

class Mylog:

    def __init__(self):
        # 创建logger对象
        self.logger = logging.getLogger('log')

    def set_msc(self,msc,level):
        try:
            # 创建文件handle
            now_date = time.strftime('%Y-%m-%d', time.localtime())
            fh = logging.FileHandler('../../log/mylog_' + now_date + '.log',encoding='gbk')
            # # 创建log对象
            # logger=logging.getLogger('log')
            # 创建控制台handle
            ch = logging.StreamHandler()

            # 格式化方法
            fm = logging.Formatter('%(levelname)s %(message)s %(asctime)s')
            # 文件格式化
            fh.setFormatter(fm)
            # 控制台格式化
            ch.setFormatter(fm)

            # 文件加入logger
            self.logger.addHandler(fh)
            # 控制台加入logger
            self.logger.addHandler(ch)

            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)

            if level=='debug':
                self.logger.debug(msc)
            elif level=='info':
                self.logger.info(msc)
            elif level=='warning':
                self.logger.warning(msc)
            elif level=='error':
                self.logger.error(msc)

            # 移除logger对象
            self.logger.removeHandler(fh)
            self.logger.removeHandler(ch)
        except:
            print('exception!')
        finally:
            # 关闭文件
            fh.close()

