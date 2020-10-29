import xlrd

# # 获取工作簿对象
# workbook=xlrd.open_workbook('C:\\Users\\zengchongliner\\Desktop\\其他\\pycharmexl.xlsx')
# # 获取工作表
# sheet1=workbook.sheet_by_name('Sheet1')
# # 获取单元格
#
# for row in range(0,sheet1.nrows):
#     for col in range(0,sheet1.ncols):
#         print(sheet1.cell_value(row, col))
# value11=sheet1.cell_value(1,2)
# value00=sheet1.cell_value(0,0)
# value10=sheet1.cell_value(1,0)
#
# print(value00)
# print(value11)
# print(value10)

class Excel_Operation:

    def __init__(self,path,sheet_name):
        # 获取工作簿对象
        self.workbook=xlrd.open_workbook(path)
        # 获取工作表
        self.sheet1=self.workbook.sheet_by_name(sheet_name)
        # 获取单元格

        # for row in range(0,self.sheet1.nrows):
        #     for col in range(0,self.sheet1.ncols):
        #         print(self.sheet1.cell_value(row, col))
        #
    def get_nrow(self):
        return self.sheet1.nrows

    def get_ncol(self):
        return self.sheet1.ncols

    def get_cell(self,row,col):
        cell_v=self.sheet1.cell_value(row,col)
        if cell_v=='null':
            cell_v=''
        # else:
        #     str(cell_v)
        return cell_v


