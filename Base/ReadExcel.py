# -*- coding: utf-8 -*-
# @File    : ReadExcel.py
import os
import xlrd
from xlutils.copy import copy
from Base.operation_excel import OperationExcel

class ReadExcel(object):
    def __init__(self,file):
        self.OperaExcel = OperationExcel(file)

    def Read_Total_Data(self,Total_Data=None):
        '''获取整个excel中sheet页面中的数据'''
        if Total_Data is None:
            Total_Data = []

        '''首先获取文件中sheet的数量'''
        sheet_numbers = self.OperaExcel.get_sheet_number()
        '''获取总的数据'''
        for sheet_number in range(sheet_numbers):
            '''获取页面行数'''
            nrows = self.OperaExcel.get_lines(sheet_number)
            for row in range(1,nrows):
                Total_Data.append(self.OperaExcel.get_row_value(sheet_number,row))
        return Total_Data





