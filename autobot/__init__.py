import socket


class Autobot():
    def __init__(self, host, channel, name, port=6667, log=False):
        self.HOST = host
        self.PORT = port
        self.CHANNEL = channel
        self.NICK = name
        self.IDENT = name
        self.REALNAME = name
        self.log = log
        self.buffer = ""

        try:
            self.irc = socket.socket()
            self.irc.connect((self.HOST, self.PORT))
            self.irc.send(("NICK %s\r\n" % self.NICK).encode())

            self.irc.send(("USER %s %s bla :%s\r\n" % (self.IDENT,
                          self.HOST,
                          self.REALNAME)).encode())
            self.irc.send(("JOIN %s\r\n" % self.CHANNEL).encode())

        except Exception as e:
            print(e)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.irc.shutdown(2)
        self.irc.close()

    def read(self):
        self.buffer = self.irc.recv(1024).decode('utf-8')
        if self.log:
            with open(self.log, 'a') as f:
                f.write(self.buffer)

        parts = self.buffer.split()
        if len(parts) == 2:
            msg = {
                'full': self.buffer,
                'source': parts[1],
                'command': parts[0],
                'nick': '',
                'message': ''
            }
        else:
            msg = {
                'full': self.buffer,
                'source': parts[0],
                'command': parts[1],
                'nick': parts[2],
                'messsage': parts[3:len(parts)]
            }

        if msg['command'] == 'PING':
            self.send("PONG")

        return msg

    def send(self, msg):
        if self.log:
            with open(self.log, 'a') as f:
                f.write(msg + "\n")

        self.irc.send(msg.encode())
