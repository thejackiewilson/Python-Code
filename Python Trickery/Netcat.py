import argparse 
import socket
import shlex
import subprocess 
import sys
import textwrap
import threading

class NetCat: 
    def __init__(self, args, buffer=None): 
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()
            
    def send(self): 
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
    
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()
            
    def listen(self):
        target = self.args.target
        port = self.args.port
        self.socket.bind((target, port))
        self.socket.listen(5)
        
        print(f'Listening on {target}:{port}...')
        client_socket, address = self.socket.accept()
        print(f'Accepted connection from {address[0]}:{address[1]}')
        
        if self.args.command:
            while True:
                client_socket.send('BHP:# '.encode())
                cmd_buffer = ''
                while '\n' not in cmd_buffer:
                    cmd_buffer += client_socket.recv(1024).decode()
                response = execute(cmd_buffer)
                client_socket.send(response.encode())
        elif self.args.upload:
            file_buffer = ''
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                else:
                    file_buffer += data.decode()
            try:
                with open(self.args.upload, 'wb') as f:
                    f.write(file_buffer.encode())
                client_socket.send(f'Successfully saved file to {self.args.upload}'.encode())
            except:
                client_socket.send(f'Failed to save file to {self.args.upload}'.encode())
        elif self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
        else:
            while True:
              data = client_socket.recv(1024).decode()
              if not data:
                    break
              else:
                    print(data)


def execute(cmd):
    cmd =cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    
    return output.decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example: Netcat.py -t 192.168.1.108 -p 5555 -l -c 
                               # command shell 
                               Netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt 
                               # upload to file 
                               Netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat/etc/passwd\" 
                               # execute command
                               echo 'ABC' | ./Netcat.py -t 192.168.1.108 -p 135 
                               # echo text to server port 135
                               Netcat.py -t 192.168.1.108 -p 5555 
                               # connect to server'''))
    
parser.add_argument('-c', '--command', action='store_true', help='command shell')
parser.add_argument('e', '--execute', help='execute specified command')
parser.add_argument('-l', '--listen', action='store_true', help='listen')
parser.add_argument('-p', '--port', type=int, default=5555, help='specificed port')
parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
parser.add_argument('-u', '--upload', help='upload file')
args = parser.parse_args()
if  args.listen:
    buffer= ''
else:
    buffer = sys.stdin.read()
    nc = NetCat(args, buffer.encode())
nc.run()
