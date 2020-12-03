import socket

host = "192.168.1.19"
port = 80
headers = """\
GET /5/{state} HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Referer: {referer}\r 
Save-Data: {data}\r
Host: {host}\r
Connection: close\r
\r\n"""

# class Request(self):
def setState(state):
    body_bytes = state.encode('ascii')
    header_bytes = headers.format(
        state=state,
        content_type="application/x-www-form-urlencoded",
        content_length=len(body_bytes),
        referer="http://192.168.1.19/5/"+state,
        data = state,
        host=str(host) + ":" + str(port)
    ).encode('iso-8859-1')
    payload = header_bytes + body_bytes
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(payload)

# New Client.
# GET /5/off HTTP/1.1
# Host: 192.168.1.19
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# Save-Data: on
# User-Agent: Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Referer: http://192.168.1.19/5/on
# Accept-Encoding: gzip, deflate
# Accept-Language: cs-CZ,cs;q=0.9,en;q=0.8,sk;q=0.7