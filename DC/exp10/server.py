import socket
import os
from threading import Thread
import threading
clients = set()
clients_lock = threading.Lock()


def thread_listener(conn, address):
    conn.send(bytes(str("name?"), 'utf-8'))
    data = str(conn.recv(1024), 'utf-8')
    print(f"{data} has joined !!!")
    with clients_lock:
        clients.add(conn)
    try:
        while True:
            data = ""
            conn.send(bytes(str("msg?"), 'utf-8'))
            data = str(conn.recv(1024), 'utf-8')
            print(f"Master has sent  >>>> {data[4:]} <<<< to all the slaves")
            if not data:
                break
            else:
                # print(repr(data))
                with clients_lock:
                    for c in clients:
                        c.sendall(bytes(str(data), 'utf-8'))
    finally:
        with clients_lock:
            clients.remove(conn)
            client.close()


def server():
    HOST = socket.gethostname()
    PORT = 1298
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(3)
    th = []

    while True:
        print(f"Server is listening for connections running at port {PORT}")
        client_conn, address = s.accept()
        th.append(Thread(target=thread_listener,
                         args=(client_conn, address)).start())

    s.close()


if __name__ == '__main__':
    server()
