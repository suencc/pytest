from flask import Flask, Response
from flask_restaction import Api, abort

app = Flask(__name__)
# 创建一个 Api 对象，把 app 作为参数
api = Api(app)

# 创建 Welcome 类，描述欢迎信息(框架可以序列化任意类型的对象)
class Welcome:

    def __init__(self, name):
        self.name = name
        self.message = "Hello %s, Welcome to flask-restaction!" % name
    def foo(self):
        print("test for sire")
    count =100

# 创建一个 Hello 类，定义 get 方法
class Hello:
    """Hello world"""

    # 在 get 方法文档字符串中描述输入参数和输出的格式
    def get(self, name):
        """
        Get welcome message

        $input:
            name?str&default="world": Your name
        $output:
            message?str: Welcome message
        $error:
            400.InvalidData: 输入参数错误
            403.PermissionDeny: 权限不足
            501.xxx: xxx
            404.yyy: yyy
        """
        return Welcome(name)
        ##return "22"
        #return "400"
        #abort(404)
        #abort(404,Response())
        #abort(501, "error", "Server error")

# 添加资源
api.add_resource(Hello)
# 配置API文档的访问路径
app.route('/')(api.meta_view)

if __name__ == '__main__':
    app.run()