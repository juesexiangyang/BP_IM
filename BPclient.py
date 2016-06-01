from socket import *

client = socket(AF_INET,SOCK_DGRAM)

addr = ('10.19.22.48',50000)
try:
    while True:
        sendmsg = raw_input('me:')
        if not sendmsg:
            pass
        client.sendto(sendmsg,addr)

        recvmsg,addr = client.recvfrom(1024)
        if not recvmsg:
            pass
        print 'others:',recvmsg
except EOFError:
    print 'catched EOFError'
    client.close()
except KeyboardInterrupt:
    print 'catched KeyboardInterrupt'
    client.close()
