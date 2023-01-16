import http.server

class web_server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = 'File not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write('<html><body><h1>Hello, World wide web!</h1></body></html>')

httpd = http.server.HTTPServer(('', 8088), web_server)
print('Server running at localhost: 8088...')
httpd.serve_forever()
print('wow')
