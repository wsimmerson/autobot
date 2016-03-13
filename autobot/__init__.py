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
        self.irc.send('/quit'.encode())

    def read(self):
        self.buffer = self.irc.recv(1024).decode('utf-8')
        if "PING" in self.buffer:
            self.send("PONG")

        if self.log:
            with open(self.log, 'a') as f:
                f.write(self.buffer)

        return self.buffer

    def send(self, msg):
        if self.log:
            with open(self.log, 'a') as f:
                f.write(msg + "\n")

        self.irc.send(msg.encode())
