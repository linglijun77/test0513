# -*- coding: utf-8 -*-
# @File    : WriteExcel.py
import os
import xlrd,xlwt
from xlutils.copy import copy


class WriteResultData(object):
    def __init__(self,data,file):
        self.data = data
        self.file = file

        if os.path.exists(self.file):
            os.remove(self.file)

    #创建excel
    def CreateExcel(self):
        wtbook = xlwt.Workbook(encoding="utf8")
        for sheet_index in range(11):
            if sheet_index == 0:
                sheet = wtbook.add_sheet('标准问',cell_overwrite_ok=True)
                col_name = ['Index','Question','SQ','Answer','Result','Response_Answer']
                for col in range(len(col_name)):
                    sheet.write(0,col,col_name[col])
            elif sheet_index == 1:
                sheet = wtbook.add_sheet('技能',cell_overwrite_ok=True)
                col_name = ['Index','Question','Module','Result','Response_Answer']
                for col in range(len(col_name)):
                    sheet.write(0,col,col_name[col])
            elif sheet_index == 2:
                sheet = wtbook.add_sheet('机器人形象',cell_overwrite_ok=True)
                col_name = ['Index','Question','Answer','Response_Answer']
                for col in range(len(col_name)):
                    sheet.write(0,col,col_name[col])
            elif sheet_index == 3:
                sheet = wtbook.add_sheet("闲聊",cell_overwrite_ok=True)
                col_name = ["Index","Question","Result.Source",'Result','Response_Answer']
                for col in range(len(col_name)):
                    sheet.write(0,col,col_name[col])
            elif sheet_index == 4:
                sheet = wtbook.add_sheet("任务引擎", cell_overwrite_ok=True)
                col_name = ["Index", "Question", "Module", 'Answer','Result','Response_Answer']
                for col in range(len(col_name)):
                    sheet.write(0, col, col_name[col])
            elif sheet_index == 5:
                sheet = wtbook.add_sheet("指令回答", cell_overwrite_ok=True)
                col_name = ["Index", "Question", "Module", 'Answer', 'Result', 'Response_Answer']
                for col in range(len(col_name)):
                    sheet.write(0, col, col_name[col])
            elif sheet_index == 6:
                sheet = wtbook.add_sheet("敏感词回答", cell_overwrite_ok=True)
                col_name = ["Index", "Question", "Module", 'Answer', 'Result', 'Response_Answer']
                for col in range(len(col_name)):
                    sheet.write(0, col, col_name[col])
            elif sheet_index == 7:
                sheet = wtbook.add_sheet("知识图谱", cell_overwrite_ok=True)
                col_name = ["Index", "Question", 'Answer',"Module", 'Result', 'Response_Answer']
                for col in range(len(col_name)):
                    sheet.write(0, col, col_name[col])
            elif sheet_index == 8:
                sheet = wtbook.add_sheet("意图管理", cell_overwrite_ok=True)
                col_name = ["Index", "Question", 'Intent','Result', 'Response_Intent']
                for col in range(len(col_name)):
                    sheet.write(0, col, col_name[col])
            elif sheet_index == 9:
                sheet = wtbook.add_sheet("第三方闲聊", cell_overwrite_ok=True)
                col_name = ["Index", "Question", 'Answer',"Module",'Result','Response_Intent']
                for col in range(len(col_name)):
                    sheet.write(0, col, col_name[col])
            elif sheet_index == 10:
                sheet = wtbook.add_sheet("同义词转换", cell_overwrite_ok=True)
                col_name = ["Index", "Question", 'Module', "Answer", 'Result', 'Response_Intent']
                for col in range(len(col_name)):
                    sheet.write(0, col, col_name[col])

        #保存创建文件
        wtbook.save(self.file)

    def WriteExcel(self):
        self.CreateExcel()
        rb = xlrd.open_workbook(self.file)
        wb = copy(rb)
        row0 = 0
        row1 = 0
        row2 = 0
        row3 = 0
        row4 = 0
        row5 = 0
        row6 = 0
        row7 = 0
        row8 = 0
        row9 = 0
        row10 = 0

        for line in range(len(self.data)):
            row_value = self.data[line]
            row_index = row_value[0]
            if row_index == 0:
                ws = wb.get_sheet(0)
                for col,value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row0+1,col,value,self.Write_Fail())
                    else:
                        ws.write(row0+1,col,value)
                row0 += 1
            elif row_index == 1:
                ws = wb.get_sheet(1)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row1 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row1 + 1, col, value)
                row1 += 1
            elif row_index == 2:
                ws = wb.get_sheet(2)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row2 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row2 + 1, col, value)
                row2 += 1
            elif row_index == 3:
                ws = wb.get_sheet(3)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row3 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row3 + 1, col, value)
                row3 += 1
            elif row_index == 4:
                ws = wb.get_sheet(4)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row4 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row4 + 1, col, value)
                row4 += 1
            elif row_index == 5:
                ws = wb.get_sheet(5)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row5 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row5 + 1, col, value)
                row5 += 1
            elif row_index == 6:
                ws = wb.get_sheet(6)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row6 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row6 + 1, col, value)
                row6 += 1
            elif row_index == 7:
                ws = wb.get_sheet(7)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row7 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row7 + 1, col, value)
                row7 += 1
            elif row_index == 8:
                ws = wb.get_sheet(8)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row8 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row8 + 1, col, value)
                row8 += 1
            elif row_index == 9:
                ws = wb.get_sheet(9)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row9 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row9 + 1, col, value)
                row9 += 1
            elif row_index == 10:
                ws = wb.get_sheet(10)
                for col, value in enumerate(row_value):
                    if value == "Fail":
                        ws.write(row10 + 1, col, value, self.Write_Fail())
                    else:
                        ws.write(row10 + 1, col, value)
                row10 += 1

        #数据写入到excel后进行保存
        wb.save(self.file)
    def Write_Fail(self,bold=True,color=2):
        style = xlwt.XFStyle()      # 初始化样式
        font = xlwt.Font()          # 为样式创建字体
        font.name = 'Time New Roman'
        font.colour_index = color
        font.height = 200
        style.font = font

        return style






