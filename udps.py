import socket
from threading import Thread


def lissen_other(server):
    global addr 
    while True:
        message, addr = server.recvfrom(1024)
        print(addr)
        print(message.decode('utf-8'))

def lissen_me(server):
    while True:
        message = input()
        message = message.encode('utf-8')

        server.sendto(message, addr)
        #server.send(message)
    

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = int(input('Type port: '))
    addr = (socket.gethostname(), port)
    server.bind(addr)

    thr1 = Thread(target=lissen_me, args=(server, ), daemon=True)
    thr2 = Thread(target=lissen_other, args=(server, ), daemon=True)


    thr1.start()
    thr2.start()


    thr2.join()





if __name__ == '__main__':
    addr = ''
    main()




