Autobot

Context Manager for ease of creating IRC bots

Example writing room activity to a file:
```
  from autobot import Autobot

  with Autobot('irc.freenode.net', '#python', '[Wally]',
               log='transcript.log') as bot:
    while True:
      r = bot.read() #  read will write to the specified log
      if "some trigger" in r['message']:
        bot.send("some message back to the chat")
      #respond to privmsg
      if r['command'] == 'PRIVMSG':
        bot.send("some message or command")
```
