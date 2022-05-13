# -*- coding: utf-8 -*-
# @File    : operation_excel.py
import os
import xlrd
from xlutils.copy import copy


class OperationExcel(object):
    def __init__(self,file):
        self.file = file

    def get_file(self):
        '''获取文件表中的内容'''
        data = xlrd.open_workbook(self.file)

        return data

    def get_sheet_data(self,by_index):
        '''获取sheet表中的数据'''
        data = self.get_file()
        tables = data.sheets()[by_index]

        return tables

    def get_lines(self,by_index):
        '''获取sheet表中的行数'''
        line = self.get_sheet_data(by_index)
        return line.nrows

    def get_row_value(self,by_index,row):
        '''获取某一行数据'''
        row_value = self.get_sheet_data(by_index).row_values(row)
        return row_value

    def get_sheet_number(self):
        '''统计excel中有多少个sheet页面'''
        table = self.get_file()
        count = len(table.sheets())
        return count
