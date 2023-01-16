import http.server, socketserver
import cgi
import BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving at port', PORT)
    httpd.serve_forever
