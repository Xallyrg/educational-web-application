from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """Обработка входящих GET-запросов"""

    def do_GET(self):
        try:
            # Путь к файлу contacts.html (предположим, что файл лежит в папке pages рядом со скриптом)
            file_path = os.path.join("pages", "contacts.html")

            # Чтение HTML-файла
            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()

            # Отправка заголовков
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            # Отправка содержимого HTML-файла
            self.wfile.write(bytes(html_content, "utf-8"))

        except FileNotFoundError:
            self.send_error(404, "Файл не найден: contacts.html")

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
