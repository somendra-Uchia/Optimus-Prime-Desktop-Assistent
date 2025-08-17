from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
        
    def do_GET(self):
        if self.path == '/status':
            try:
                with open("../input.txt", "r") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(content.encode())
            except:
                self.send_response(404)
                self.end_headers()
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('localhost', 8000), CORSRequestHandler)
    print("UI Server running on http://localhost:8000")
    server.serve_forever() 