from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
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

    def do_POST(self):
        if self.path == "/contacts":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            post_str = post_data.decode('utf-8')
            print("Получены POST данные:", post_str)

            # Парсим данные в словарь
            post_params = parse_qs(post_str)
            print("Распарсенные параметры:", post_params)

            # Можно сформировать ответ
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            response = """
            <html>
              <body>
                <h2>Спасибо за сообщение!</h2>
                <button onclick="window.history.back()">Назад</button>
              </body>
            </html>
            """
            self.wfile.write(response.encode('utf-8'))
        else:
            # Если POST-запрос на другой путь — 404
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
