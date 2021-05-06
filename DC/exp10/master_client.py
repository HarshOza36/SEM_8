import socket


class Client_master:
    def client_master(self):
        HOST = socket.gethostname()
        PORT = 1298
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        name = "master"
        while True:
            line = (str(sock.recv(1024), 'utf-8'))
            if (line.startswith("name?")):
                sock.send(bytes(name, 'utf-8'))
            msg = input("Enter a message >>>> ")
            sock.sendall(bytes("msg?"+msg, 'utf-8'))


Client_master().client_master()
