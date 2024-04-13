##数据处理
import json

from openpyxl import Workbook
adr=".\\user\\app.json"

with open(adr,"r") as file:
    load_data_app=json.load(file)
print(load_data_app)





def write_to_excel():
    # 创建一个新的工作簿
    wb = Workbook()

    # 获取默认的工作表
    ws_default = wb.active
    ws_default.title = "Sheet1"  # 设置默认工作表的名称

    # 设置表头
    ws_default.append(['程序列表',"程序名称"])

    # 添加数据到默认工作表
    for item in load_data_app:
        ws_default.append([item])

    for col in ws_default.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2  # 调整列宽的公式，可根据需要调整
        ws_default.column_dimensions[column].width = adjusted_width

    # 保存工作簿
    wb.save('.\\user\\app.xlsx')
    print("Data has been written to data_report.xlsx")

if __name__ == "__main__":
    # 要写入的数据
   write_to_excel()

    # 写入数据到Excel文件

