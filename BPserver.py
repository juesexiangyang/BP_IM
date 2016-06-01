from socket import *

server = socket(AF_INET,SOCK_DGRAM)

server.bind(('0.0.0.0',50000))
try:
    while True:
        #print 'waiting for message...'
    
        recvmsg,addr = server.recvfrom(1024)
        #print '...connected from :',addr

        if recvmsg:
            print 'others:',recvmsg    

        sendmsg = raw_input('me:')
        if not sendmsg:
            pass
        server.sendto(sendmsg,addr)
except EOFError:
    print 'catched EOFError'
    server.close()
except KeyboardInterrupt:
    print 'catched KeyboardInterrupt'
    server.close()




