#学习目标：python 数据库的使用
#        python git的使用
import pymysql as sq
from pymysql import Connection
import configparser
if 0:
    import  pymysql as sq
    conn=sq.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        port=3306,
        db="ms_1",
        charset="utf8",
    )
    print(conn)

#.conf/.ini 文件可以作为配置文件 connect方法生成数据库对象的一些参数保存在这里
#配置文件的配置项，读取的时候默认都是以字符串类型的，对应字符串，不需要加双引号""

db_config=configparser.ConfigParser()
db_config.read_file(open("sql_1.ini",encoding="utf-8",mode="rt"))

conn:Connection=sq.connect(
    host=db_config.get('mysql', 'host'),  # 连接名称，默认127.0.0.1
    user=db_config.get('mysql', 'user'),  # 用户名
    passwd=db_config.get('mysql', 'passwd'),  # 密码
    port=int(db_config.get('mysql', 'port')),  # 端口，默认为3306
    db=db_config.get('mysql', 'db'),  # 数据库名称
    charset=db_config.get('mysql', 'charset'),  # 字符
)
print(conn)

#游标
cur=conn.cursor()
print(cur)

cur.execute("select" "


