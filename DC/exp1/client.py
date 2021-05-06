import socket


def client():
    HOST = socket.gethostname()
    PORT = 1298
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    msg = ""

    while msg != "bye":
        print("======================MENU=================")
        print("1. Addition  2. Subtraction 3.Multiplication 4.Division 5.Modulus")
        e = int(input("Enter your choice >>> "))
        n1, n2 = input("Enter 2 numbers space separated >>> ").split(" ")
        data = f"{n1} {e} {n2}"
        sock.sendall(bytes(data, 'utf-8'))
        print(str(sock.recv(1024), 'utf-8'))
        msgg = input("Enter bye to exit or Enter C to continue >>> ").lower()
        if msgg == "bye":
            sock.sendall(bytes(msgg, 'utf-8'))
            print("Server >>> Bye !!")
        msg = msgg
    sock.close()


if __name__ == '__main__':
    client()
