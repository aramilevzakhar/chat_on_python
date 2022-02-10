import socket
import threading


class MySocket(socket.socket):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)

    


#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = MySocket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((socket.gethostname(), 6666))
server.listen()


users = []
        



def listen(client, addr):
    while True:
        try:
            message = client.recv(1024)
        except Exception as e:
            print(e)
            break

        sss1 = message.decode('utf-8').split(' ')[-1]
        #print(sss1)
        print(message.decode('utf-8'))
        for user in users:
            if user != client:
                try:
                    #print(message)
                    user.send(message)
                except Exception as e:
                    print("error in send")
                    break

        if sss1 == 'exit':
            client.close()
            users.remove(client)
            break



def main():
    i = 0
    while True:

        print(i, len(users))
        client, addr = server.accept()
        users.append(client)
        i += 1


        

        print(f'Connected to {addr}')
        s = threading.Thread(target=listen, args=(client, addr), daemon=True)
        s.start()

    
        #msg = input('Type message')

        #client.send(msg.encode('utf-8'))


        #client.close()

if __name__ == '__main__':
    main()




