import player

cmdlist = '\n!exit    - Exits the chat, returning to the main menu\n' + \
          '!help    - Displays this exact list\n' + \
          '!users   - Displys a list of users in the room\n' + \
          'Anything else will be broadcast to the chatroom\n\n'

class game:
    def __init__(self, name='chat'):
        self.players = []
        self.name = name
        self.count = 0

    def addPlayer(self, p: player) -> bool:
        self.players.append(p)
        self.count  = self.count + 1
        p.sendUpdate('\nWelcome to Chat!' + cmdlist)
        print(p.name, 'joined chat')
        return True

    def removePlayer(self, p: player.player) -> int:
        self.players.remove(p)
        self.count = self.count - 1
        p.state = None
        return len(self.players)

    def updatePlayers(self, targets: [player.player], msg: str):
        for p in targets:
            p.sendUpdate(msg)

    def updateGame(self, sender: player.player, cmd: str):
        if cmd[0] == '!':
            if cmd.split()[0] == '!exit':
                sender.sendUpdate('Bye, sending you back to the main menu!')
                self.removePlayer(sender)
            elif cmd.split()[0] == '!help':
                sender.sendUpdate(cmdlist)
                print(sender.name, 'requested help')
            elif cmd.split()[0] == '!users':
                for p in self.players:
                    sender.sendUpdate(' - ' + str(p.name))
                sender.sendUpdate('\n')
                print(sender.name, 'requested chatroom list')
            else:
                sender.sendUpdate('Command not recognized, try !help for a list')
        else:
            self.updatePlayers(self.players, str(sender.name) + ': ' + cmd)