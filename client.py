import socket
import sys

target_host = sys.argv[1]  # Lista de argumentos passadas via linha de comando para o script Python
target_port = 9999  # Porta de conexão com o servidor
serverAddressPort = (target_host, target_port)  # Atribui a tupla de valores à variável serverAddressPort

cmd = str.encode(sys.argv[2])  # Lista de argumentos passados via linha de comando para o script Python

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Cria socket utilizando protocolo IPv4 e protocolo UDP

client.sendto(cmd, serverAddressPort)  # Envia conjunto de bytes (mensagens) para o socket remoto

response = client.recvfrom(8192)  # Recebe dados do socket remoto em um determinado tamanho de buffer

print(str(response[0], "utf-8"))  # Converte os bytes recebidos em string codificação UTF-8
