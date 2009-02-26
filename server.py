import sys
import launchers
from getopt import getopt
from socket import *


opts, args = getopt(sys.argv[1:], 'i:p:', ['interface=', 'port=' ])

interface = ''
port = 7421

for o, a in opts:
    if o in ('-i', '--interface'):
        interface = a
    elif o in ('-p', '--port'):
        port = int(a)

sock = socket()
sock.bind((interface, port))
sock.listen(1)

l = launchers.find_launchers()

def handle_command(client, command):
    """Handles a single command from the client"""
    global quit
    parts = command.split(' ')
    name = parts[0]
    if name == 'quit':
        quit = True
        raise Exception("Quit")
    if len(parts) < 2:
        return
    launcher = l[int(parts[1])] # Pull out the nth launcher
    args = parts[2:]
    if hasattr(launcher, name):
        method = getattr(launcher, name)
        intargs = [ float(a) for a in args ] # Try all integers, most args are!
        method(*intargs)

input_buffer = ""
def receive_command(client):
    """Receives and handles a command from the client"""
    global input_buffer
    input_buffer += client.recv(1024)
    commands = input_buffer.split("\n")
    input_buffer = commands[-1] # Yank off last element which is an incomplete command
    commands = commands[:-1] # Strip down to complete commands
    for command in commands:
        handle_command(client, command)


quit = False
while not quit:
    client, client_address = sock.accept()
    print "Client connected", client_address
    while client:
        try:
            receive_command(client)
        except Exception, e:
            print e
            client.shutdown(SHUT_RDWR)
            client.close()
            client = None

sock.close()
