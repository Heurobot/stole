import sqlite3 ##读取数据库的文件
import os
import openpyxl
import shutil

# Microsoft Edge浏览器历史记录文件路径
# history_file = os.path.expanduser('C:\\Users\\DELL\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History')
# history_file = os.path.expanduser('D:\\databin\\stole\\History')##同时使用的话，数据库被锁定

def get_broswer():
    # 获取当前用户的主目录
    user_home = os.path.expanduser("~")

    # 拼接路径
    appdata_path = os.path.join(user_home, "AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History")
    shutil.copy(appdata_path,".\\user\History")
    # 连接到历史记录数据库
    connection = sqlite3.connect(".\\user\\History")
    cursor = connection.cursor()
    # 执行SQL查询以获取浏览记录
    cursor.execute('SELECT * FROM urls')

    # 获取所有记录
    rows = cursor.fetchall()
    # 创建一个新的Excel工作簿
    workbook = openpyxl.Workbook()

    # 获取默认的工作表
    sheet = workbook.active
    sheet.title="sheet1"
    # 输出浏览记录
    for row in rows:
        print(row)
        # 添加一行数据
        sheet.append(row)

    for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2  # 调整列宽的公式，可根据需要调整
        sheet.column_dimensions[column].width = adjusted_width

    # 保存工作簿
    workbook.save('.\\user\\web.xlsx')


    connection.close()