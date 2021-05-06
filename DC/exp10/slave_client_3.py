import socket


class Client_three:
    def client_three(self):
        HOST = socket.gethostname()
        PORT = 1298
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        name = "Slave3"
        while True:
            line = (str(sock.recv(1024), 'utf-8'))
            if (line.startswith("name?")):
                sock.sendall(bytes(name, 'utf-8'))
            elif(line.startswith("msg?")):
                print(line[4:])
            # if(name.startswith("master")):
            #     msg = input("Enter a message >>>> ")
            #     sock.sendall(bytes("msg?"+msg, 'utf-8'))


Client_three().client_three()
