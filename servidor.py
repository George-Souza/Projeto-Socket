#!/usr/bin/env python3
import socket
import threading

# A função convert_to_bin recebe um número decimal e retorna sua versão binária
def convert_to_bin(num):
    deci = int(num)
    binario = ""
    while deci > 0:
        binario += str(deci % 2)
        deci //= 2
    return binario[::-1]

# server_name recebe o endereço ip da máquina
server_name = socket.gethostbyname(socket.gethostname()) 
# server_port armazena a porta 50000 para o socket
server_port = 50000

# criamos o socket e o associamos à tupla com o endereço e a porta
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_name, server_port))

def lida_cliente(conn, adress):
    # mostramos o endereço de conexão
    print(f"Conectado em {adress}")
    
    while True:
        # recebemos a mensagem do cliente
        entrada = conn.recv(1024)
        # caso não haja entrada, fechamos a conexão e saímos do loop
        if not entrada:
            print(f"Fechando conexão em {adress}")
            conn.close()
            break
        # a entrada é enviada para a função convert_to_bin
        # seu retorno é armazenado na variável "resposta"
        resposta = convert_to_bin(entrada)
        # enviamos a resposta na forma de bytes de volta para o cliente
        conn.sendall(str.encode(resposta))
    

# a função início é a porta de entrada da aplicação
def inicio():
    # colocamos o servidor para receber conexões
    server_socket.listen()
    print("O servidor está pronto para receber")

    while True:
        # recebemos a conexão e associamos às duas variáveis
        conn, adress = server_socket.accept()
        # abrimos uma thread que irá lidar com aquele cliente
        thread = threading.Thread(target=lida_cliente, args=(conn, adress))
        # inciamos a thread
        thread.start()
        # o número de conexões ativas é exibido na tela
        print(f"Conexões ativas: {threading.activeCount() - 1}")


inicio()
