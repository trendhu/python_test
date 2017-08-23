import pymysql.cursors

#连接数据库
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="hadoop",
    db="python",
    charset="utf8"
)

class tit:
    def __init__(self, id, title):
        self.title = title
        self.id = id




curso = conn.cursor()

#创建表
# sql = "create table todo(id int auto_increment, title TEXT, primary key(id))"
# curso.execute(sql)


#删除数据
def del_todo(id):
    sql = "delete from todo where id="+str(id)
    curso.execute(sql)
    conn.commit()


# 创建新的数据
def new_todo(text):
    print("传过来的是：",text)
    sql = "insert into todo (title) values ('" + text + "')"
    curso.execute(sql)
    conn.commit()



# 获取所有数据
def get_todos():
    print("开始查询数据")
    sql = "select *from todo"
    curso.execute(sql)
    todos = []
    for row in curso.fetchall():
        a = tit(row[0], row[1])
        todos.append(a)
        # print(row)
        # todo = {'title':row[1], 'id':row[0]}

    print(todos)
    return todos













