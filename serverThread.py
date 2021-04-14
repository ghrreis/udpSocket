import subprocess
import socket
import threading

bind_ip = "0.0.0.0"  # Aceita conexão de qualquer origem
bind_port = 9999  # Porta que o servidor "escuta"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Cria socket utilizando protocolo IPv4 e protocolo UDP

server.bind((bind_ip, bind_port))  # Atribui ao socket endereço e porta de conexão

print("[*] Listening on", bind_ip, ":", bind_port)  # Imprime os endereços IP e Porta que o servidor está sendo executado


def handle_client(msg):
    print("[*] Received:", msg)  # Imprime a mensagem recebida

    result = subprocess.run(msg, stdout=subprocess.PIPE)  # Executa o comando no terminal do SO e retorna o resultado

    server.sendto(result.stdout, bytesAddressPair[1])  # Envia conjunto de bytes (mensagens) para o socket remoto


while True:
    bytesAddressPair = server.recvfrom(8192)  # Recebe dados do socket remoto em um determinado tamanho de buffer

    print("[*] Accepted connection from:", format(bytesAddressPair[1]))  # Imprime os endereços IP e Porta respectivamente

    print("Command:", str(bytesAddressPair[0], "utf-8"))  # Imprime o comando recebido do socket remoto

    # Cria uma thread passando como parâmetros a função handle_client e o comando recebido do socket remoto
    client_handler = threading.Thread(target=handle_client, args=(str(bytesAddressPair[0], "utf-8").split(" "),))
    client_handler.start()  # Inicia a thread
