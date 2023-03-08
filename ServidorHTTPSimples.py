import socket
import os

# Define host e porta do socket
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

#usando a biblioteca OS para abrir corretamente o arquivo html
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Cria socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Espera pela conexão de cliente
    client_connection, client_address = server_socket.accept()

    # Pega a request do cliente
    request = client_connection.recv(1024).decode()
    print(request)

    # Lê pagina html que será mandada como resposta
    with open(os.path.join(__location__, 'pagina.html'), 'r', encoding="utf-8") as f:
        html_content = f.read()

    # Manda resposta HTTP, contendo a primeira linha da resposta para que a página seja exibida corretamente
    http_response = """\
HTTP/1.1 200 OK
Content-type: text/html


{}
""".format(html_content)
    client_connection.sendall(http_response.encode())
    client_connection.close()



