
# http://forums.cgsociety.org/showthread.php?f=89&t=1322430

import socket
import sys

HOST, PORT = "localhost", 32313
#data = " ".join(sys.argv[1:])

for i in range(1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))

        #data = b'<font size="6" face="Consolas" color="yellow">|hi from client '
        #data = b'|hi'
        data = b'|hi\n'
        #data = b'|\n'
        sock.sendall(data)

        #received = sock.recv(1024)
    except Exception as ex:
        print( ex )
        sys.exit(0)
    finally:
        sock.close()

    print( "Sent:     {}".format(data) )
    #print( "Received: {}".format(received) )