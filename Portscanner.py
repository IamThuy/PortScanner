import socket
import sys

"""""
Esse portscanner é básico; eu só fiz para entender como funcionam os argumentos e 
a biblioteca sys.

||| ATENÇÃO |||

A Prática de QUALQUER tipo de portscanner sem permissão é CRIME.
Eu NÃO incentivo QUALQUER tipo de ato antiético ou ILEGAL;
isso foi feito apenas para ESTUDOOOOOO. ENTENDEU? ESTUDOOOOOOOOOOOOOOOO
"""""


def scanner(remote_host):
    try:
        for port in range(1, 200):
            requisicao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data = requisicao.connect_ex((remote_host, port))
            if data == 0:
                print(f"[+] Port {port}  open :::: {socket.getservbyport(port)}")
            else:
                print("Fechado")
    except socket.gaierror:
        print("Host não encontrado")
        exit()
    except socket.error:
        print("erro durante o socket")
        exit()
    return




def main():
    if sys.argv[1] == '-help':
        print('Portscanner.py [target]')
    else:
        remote_host = sys.argv[1]
        scanner(remote_host)

    
main()
