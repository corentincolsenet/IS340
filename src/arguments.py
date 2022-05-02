from curses.ascii import isalpha
from player import Player
from player import Player, PLAYER_TYPE_AI, PLAYER_TYPE_REAL

# Basical parsing of the arguments
def checkArguments(args):
    nbArgs = len(args);
    if nbArgs > 3:
        print('Too many arguments');
        return 84;
    if nbArgs == 3:
        if args[1].isalpha() == False or args[2].isalpha() == False:
            print('One of the player name is incorrect, it should only be alpha characters');
            return 84;
    if nbArgs == 2:
        if args[1].isalpha() == False:
            print('One of the player name is incorrect, it should only be alpha characters');
            return 84;

# Generate the list of players(IA or real player depending on arguments)
def generatePlayers(args):
    players = [];
    i = 0;
    
    for x in range(1, len(args)):
        players.append(Player(PLAYER_TYPE_REAL, args[x]))

    if len(players) < 2:
        while len(players) < 2:
            players.append(Player(PLAYER_TYPE_AI, 'Player ' + str(i + 1)));
            i += 1;

    return players;