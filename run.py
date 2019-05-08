#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

def grabIndex():
    a=open("index.html","r")
    ret=a.read()
    a.close()
    return(ret)
siteStuff=grabIndex()

def grabPost():
    a=open("post.html","r")
    ret=a.read()
    a.close()
    return(ret)
postSite=grabPost()

class S(BaseHTTPRequestHandler):
    global siteStuff, postSite
    try:
	a=open("index.html","r")
	siteStuff=a.read()
	a.close()
    except:
	print("index not found")
	siteStuff="<html>site is empty</html>"
    print("got index")
    try:
	a=open("post.html","r")
	postSite=a.read()
	a.close()
    except:
	print("post not found")
	postSite="<html>post response\ndata: "


    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
	self._set_headers()

    def do_GET(self):
	global siteStuff
        self._set_headers()
        self.wfile.write(siteStuff)

    def do_POST(self):
	global postSite
        content_length = int(self.headers['Content-Length'])
	post_data = self.rfile.read(content_length)
	self._set_headers()
	self.wfile.write(postSite+post_data.encode()+"</html>")
	print(post_data.encode())

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
	run()
