import socket
from threading import Thread
import multiprocessing 
import time
import sys



class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None, daemon=False):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def lissen_server(client):
    msg1 = 0
    acc = 0
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
        except:
            print('Error')
            break

        if msg1 == msg:
            acc += 1
        else:
            acc = 0

        if acc == 100:
            #break
            #sys.exit()
            #sys.exit()
            raise SystemExit

        msg1 = msg
        print(acc, msg)


def lissen_me(client, myname):
    while True:
        msg = input()

        res = "[ " + myname + " ]: " + msg


        try:
            client.send(res.encode('utf-8'))
        except:
            print('Error')

            break
        if msg == 'exit'.lower():
            break


def main(client):
    myname = input('Type your name: ')


    try:
        s1 = Thread(target=lissen_server, args=(client, ), daemon=True)
        s2 = Thread(target=lissen_me, args=(client, myname, ), daemon=True)

        s1.start()
        s2.start()

        s1.join()
        #print(s1.run())
        #s2.join()

    except KeyboardInterrupt:
        res = "[ " + myname + " ]: exit"
        client.send(res.encode('utf-8'))

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostname(), 6666))
    main(client)





