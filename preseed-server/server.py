from http.server import BaseHTTPRequestHandler, HTTPServer
import random

with open("./example-preseed.txt", "r")  as f:
  preseed_file = f.read()

with open("./names.txt", "r")  as f:
  available_names = f.read().splitlines()
  random.shuffle(available_names)


try:
  with open("./hosts", "r") as f:
    processed_ips = list(map(lambda x: x.split()[1], f.read().splitlines()))
except:
  processed_ips = []

print(processed_ips)

hosts = open("./hosts", "a")

class CustomHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    client_ip = self.client_address[0]
    if client_ip in processed_ips:
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(b"<h1>Preseed already set</h1>")
      return

    processed_ips.append(client_ip)
    hostname = available_names.pop()
    content = preseed_file.replace("__HOSTNAME__", hostname )
    hosts.write(f"{hostname} {client_ip}\n")


    self.send_response(200)
    self.send_header("Content-type", "text/plain")
    self.end_headers()
    self.wfile.write(content.encode())

server_address = ("", 8080)  # Serve on port 8080
httpd = HTTPServer(server_address, CustomHandler)
print("Serving on port 8080...")
httpd.serve_forever()

