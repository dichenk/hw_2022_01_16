import http.server

class GP(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self._set_headers()
        print(self.path)
        self.wfile.write('<html><body><h1>Hello, World wide web!</h1></body></html>')

def run(server_class=http.server.HTTPServer, handler_class=GP, port=8088):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Server running at localhost: 8088...')
    httpd.serve_forever()

run()
