import pymysql.cursors

#数据库名
DATABASE_NAME = 'python'

#数据库IP
HOST = 'localhost'

#端口号
PORT = 3306

#用户名
USER_NAME = 'root'

#数据库密码
PASSWORD = 'hadoop'

#数据库编码
CHAR_SET = 'utf8'


#连接MySQL服务
conn = pymysql.Connect(
    host = HOST,
    port = PORT,
    user = USER_NAME,
    passwd = PASSWORD,
    db = DATABASE_NAME,
    charset = CHAR_SET
)

# handel 获取数据库的句柄(好进行进一步的操作)
cursor = conn.cursor()

#创建一个名字叫做 python 的数据库
# sql ="CREATE DATABASE python"

# sql = "CREATE TABLE Student_2(name varchar(10) not null primary key, arg int(3) not null, sex varchar(4) not null, datetime timestamp)"
# sql_2 = '''
#         CREATE TABLE `Student` (
#         `id` int(11) NOT NULL,
#         `name` varchar(20) NOT NULL,
#         `age` int(11) DEFAULT NULL,
#         PRIMARY KEY (`id`),
#         UNIQUE KEY `name` (`name`)
#         ) ENGINE=InnoDB DEFAULT CHARSET=utf8
#      '''

#插入数据
# sql = "insert into Student_2 (name, arg, sex) values ('zhangsan', 13, 'nan')"

sql = "insert into Student_2 (name, arg, sex) values ('xiaoming', 20, 'nan')"

# sql = "SELECT * FROM Student_2"

cursor.execute(sql)
conn.commit()

# for row in cursor.fetchall():
#     print(row)












