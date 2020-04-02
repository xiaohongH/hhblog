# hello.py
def application1(environ, start_response):
    qstr = environ.get('PATH_INFO')
    print (qstr)
    if qstr == "/":
        start_response('200 ok',[('Content-Type','text/html')])
        return [b'<h1>Hello, Web!</h1>']
    else:
        start_response('404 ok',[('Content-Type','text/html')])
        return [b'<h1>404</h1>']
        
def application():
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method=='GET' and path=='/':
        return handle_home(environ, start_response)
    if method=='POST' and path='/signin':
        return handle_signin(environ, start_response)