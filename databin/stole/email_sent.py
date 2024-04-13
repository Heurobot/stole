import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(filename, recipient_email):
    # 邮件参数
    sender_email = "xxx"  # 发件人邮箱地址
    sender_password = "xxx"  # 发件人邮箱密码
    smtp_server = "smtp.gmail.com"  # SMTP服务器地址
    smtp_port = 587  # SMTP服务器端口号

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "File Attachment"

    # 添加文件附件
    with open(filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {filename}')
    msg.attach(part)

    # 连接到SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", str(e))
    finally:
        server.quit()

if __name__ == "__main__":
    filename = "file_to_send.txt"  # 要发送的文件名
    recipient_email = "recipient@example.com"  # 接收者邮箱地址
    send_email(filename, recipient_email)
