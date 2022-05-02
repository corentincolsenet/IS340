from sys import argv
from arguments import checkArguments, generatePlayers
from game import Game
from player import Player, PLAYER_TYPE_AI, PLAYER_TYPE_REAL

def main():
    if checkArguments(argv) == 84:
        return 84;
    players = generatePlayers(argv)
    # game = Game(players[0], players[1]);
    return 0;

if __name__ == "__main__":
    main()