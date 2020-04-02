# 从wsgiref导入
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数
from hello import application 

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
http = make_server('', 8890, application)
print ('Servering HTTP on port 8000...')

# 开始监听HTTP请求
http.serve_forever()
