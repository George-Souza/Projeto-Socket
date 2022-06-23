#!/usr/bin/env python3
import socket

# Associamos o endereço do servidor (o mesmo da máquina)
server_name = socket.gethostbyname(socket.gethostname())
# e associamos a porta do servidor
server_port = 50000
# tudo isso é armazenado em uma tupla
addres = (server_name, server_port)

# criamos o socket cliente e o conectamos ao servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addres)

# a mensagem exibe o que a aplicação faz
print("A seguinte aplicação recebe um número decimal como entrada e retorna seu equivalente binário")
# recebemos a entrada do cliente e a enviamos para o servidor
mensagem = input("Digite o número: ")
client_socket.sendall(str.encode(mensagem))

# recebemos a resposta do cliente e a exibimos na tela
resposta = client_socket.recv(1024)

print(f"Número na forma binária: {resposta.decode()}")

# por fim, fechamos o socket
client_socket.close()
