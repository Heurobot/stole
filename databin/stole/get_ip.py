import socket
import json
import openpyxl

def get_ip():
    user_ip=[]
    hostname=socket.gethostname()
    ip_address=socket.getaddrinfo(hostname,None)
    print(hostname)
    for i in ip_address:
        print(i,"\n")
        user_ip.append(i)
    print(user_ip)

    adr=".\\user\\ip.json"
    with open(adr,"w") as file:
        json.dump(user_ip,file)

    with open('.\\user\\ip.txt', 'w') as file:
        # 将数据写入文件
        for item in user_ip:
            file.write(str(item) + '\n')

# with open(adr,"r") as file:
#     load_data=json.load(file)
# print(load_data,"这是读取的数据")
