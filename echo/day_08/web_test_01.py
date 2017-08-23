import web

urls = (
    #一个 路径 对应一个 类名 , 在这里面/就是路径 index 是类名
    "/", "index"
)

#设置模板渲染路径
reder = web.template.render("templates/")

class index:
    #方法名叫做 GET , 表示浏览器调用 GET 方法
    def GET(self):
        # return "hello this is index"
        # return reder.js_01()
        
        # name = "hadoop"
        # return reder.hello(name)

        a = web.input(name=None)
        return reder.hello(a.name)




if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()















