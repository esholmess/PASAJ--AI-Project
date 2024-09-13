from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Tarih kontrolü ve yönlendirme
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        simdiki_tarih = datetime.now()
        # Eğer tarih 1 Ocak ise, dbayram.html sayfasına yönlendir
        if simdiki_tarih.month == 5 and simdiki_tarih.day == 5:
            with open("dbayram/dbayram.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            with open("main2/main2.html", "rb") as file:
                self.wfile.write(file.read())

# Sunucu başlatma
httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
print("Sunucu başlatıldı.")
httpd.serve_forever()
