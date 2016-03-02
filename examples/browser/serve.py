#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()

        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")

PORT = 9000

httpd = SocketServer.TCPServer(("", PORT), MyHTTPRequestHandler)

print "serving at port", PORT
httpd.serve_forever()