import xlrd
import xlwt





class OperationExcel():
    def __init__(self, file_name=None, sheet_id=None,sheet_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = '../data/case.xlsx'
        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0
        if sheet_name:
            self.sheet_name = sheet_name
        else:
            self.sheet_name = "login"

        self.sheet = self.__get_sheet_data()

    # 获取sheets的句柄 内容
    def __get_sheet_data(self):
        self.data = xlrd.open_workbook(self.file_name)
        sheet = self.data.sheet_by_index(self.sheet_id)
        # self.data = load_workbook(self.file_name)
        # sheet = self.data.get_sheet_by_name(self.sheet_name)
        return sheet

    # 获取sheet name
    def get_sheet_name(self):
        return self.data.sheet_names()[self.sheet_id]         #这 xlrd
        # return self.sheet_name

    # 获取该sheet单元格的总行数
    def get_sheet_rows_num(self):
        return self.sheet.nrows

    # 获取该sheet单元格的总列数
    def get_sheet_cols_num(self):
        return self.sheet.ncols

    # 获取该sheet单元个的内容
    def get_cell_value(self, row, col):
        return self.sheet.cell_value(row, col)

    # 获取该sheet 指定行的所有内容
    def get_row_value(self, row):
        return self.sheet.row_values(row)
        # return self.sheet

    # 获取该sheet 指定列的所有内容
    def get_col_value(self, col):
        return self.sheet.col_values(col)

    def write_cell_value(self,row,col):
        workbook = xlwt.Workbook()
        worksheet  = workbook.add_sheet(self.get_sheet_name())
        print(self.get_sheet_name())
        worksheet.write(row,col,'aaaaaa')
        workbook.save(self.file_name)

if __name__ == '__main__':
    import time

    print(time.time())
    ex = OperationExcel(file_name='../data/case2.xlsx')
    print(ex.get_row_value(0))
    print(ex.get_sheet_name())
    # ex.write_cell_value(0,0)
    print(time.time())


#book = xlrd.open_workbook('../data/case.xlsx')  # 得到excel文件的操作对象
# #得到sheet对象
# sheet0 = book.sheet_by_index(0)     #通过sheet索引 得到sheet对象
# sheet_name = book.sheet_names()[0]  #获得指定 索引的sheet名字
# d = book.sheets()[0]
# print(d.ncols)
# print(sheet_name)
#
# sheet1 = book.sheet_by_name('test')        #通过sheet名字来获取，
#
# nrows = sheet0.nrows    #行总数
# ncols = sheet0.ncols
# print(nrows,ncols)
#
# #获得指定的行、列的值，
# row_data = sheet0.row_values(0)
# col_data = sheet0.col_values(0)
# print(row_data,'\n',col_data)
#
# #获取某个表格内容
# cell_value= sheet0.cell_value(0,0)
# print(cell_value)
