import http.server
import json

from parse_data import parse_ecowitt_data
from send_data import insert_data

PORT = 8020
Handler = http.server.SimpleHTTPRequestHandler


class WeatherDataHandler(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        length = int(self.headers.get("content-length", 0))
        data = self.rfile.read(length)
        self._set_response()
        parsed = parse_ecowitt_data(data.decode("utf-8"))
        insert_data(parsed)

    def do_POST(self):
        self.do_GET()



if __name__ == '__main__':
    with http.server.HTTPServer(("0.0.0.0", PORT), WeatherDataHandler) as httpd:
        print(f"serving at port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
