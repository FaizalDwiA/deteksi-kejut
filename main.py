import os
import webbrowser
import threading
import ssl
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Tentukan lokasi root proyek (satu level di atas folder 'server/')
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Fungsi untuk menjalankan server HTTPS
def run_server():
    PORT = 174

    # Pindah ke root project agar server bisa membaca index.html di root
    os.chdir(ROOT_DIR)

    # Konfigurasi handler
    handler = SimpleHTTPRequestHandler
    httpd = HTTPServer(("localhost", PORT), handler)

    # Tambahkan SSL
    key_path = os.path.join(os.path.dirname(__file__), "key.pem")
    cert_path = os.path.join(os.path.dirname(__file__), "cert.pem")

    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=key_path, certfile=cert_path, server_side=True)

    print(f"🔒 Server HTTPS berjalan di https://localhost:{PORT}")
    httpd.serve_forever()

# Fungsi untuk membuka browser otomatis
def open_browser(url):
    webbrowser.open(url)

# Jalankan server di thread terpisah
server_thread = threading.Thread(target=run_server)
server_thread.daemon = True
server_thread.start()

# Buka browser ke halaman utama
open_browser('https://localhost:174')

# Tetap menjalankan server
server_thread.join()
