from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'Test': 'this is a testing message, YEE'}
host = ('localhost', 8000)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    try:
        server = HTTPServer(host, RequestHandler)
        print("Starting http server listening at: %s:%s" % host)
        server.serve_forever()

    except KeyboardInterrupt:
	    print("Ctrl-C received, server shutting down...")
	    server.socket.close()