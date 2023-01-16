from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8080

class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("<p>Hello, World wide web!</p>", "utf-8"))

httpd = HTTPServer((hostName, serverPort), web_server)
print('Server running at localhost: 8080...')
httpd.serve_forever()