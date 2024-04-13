import winreg
import json
# 定义Windows注册表中存储应用程序信息的键路径
def get_app():
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    applist=[]
    # 打开注册表键
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)

    # 获取子键数量
    num_subkeys = winreg.QueryInfoKey(key)[0]

    # 遍历每个子键
    for i in range(num_subkeys):
        subkey_name = winreg.EnumKey(key, i)
        subkey_path = key_path + "\\" + subkey_name

        try:
            # 尝试读取DisplayName值
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as subkey:
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                print(display_name)
                applist.append(display_name)
        except FileNotFoundError:
            continue

    # 关闭注册表键
    winreg.CloseKey(key)
    print(applist)##列表来储存获取到的qpp

    adr=".\\user\\app.json"
    with open(adr,"w") as file:
        json.dump(applist,file)

# with open(adr,"r") as file:
#     load_data=json.load(file)
# print(load_data,"这是读取的数据")