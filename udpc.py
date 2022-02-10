import socket
import base64
import pyautogui
from threading import Thread

def lissen_me(client, fport):
    x = 0; y = 0

    while True:
        #message = input()
        #port = int(input('type port for sending: '))
        x1, y1 = pyautogui.position()
        if not (x1 == x or y1 == y):
            x = x1 ; y = y1
            message = str.format('X: {0}, Y: {1}', x1, y1)
            message = message.encode('utf-8')
            #message = base64.b64encode(message)
            addr = (socket.gethostname(), fport)
            client.sendto(message, addr)

def lissen_server(client):
    while True:
        getting_message = client.recvfrom(1024)
        print(getting_message)



#base64.b64encode(s)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #yport = int(input('Type the port for yourself: '))
    #fport = int(input('Type the port for your freind: '))
    yport = 9999
    fport = 8888

    client.bind((socket.gethostname(), yport))

    thr1 = Thread(target=lissen_me, args=(client, fport), daemon=True)
    thr2 = Thread(target=lissen_server, args=(client, ), daemon=True)


    thr1.start()
    thr2.start()


    thr2.join()



if __name__ == '__main__':
    main()












