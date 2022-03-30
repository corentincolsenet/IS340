from inspect import getargs
from typing import get_args
from game import Game
from player import Player, PLAYER_TYPE_AI, PLAYER_TYPE_REAL

def main():
    player1 = Player(PLAYER_TYPE_REAL, 'Kylian')
    player2 = Player(PLAYER_TYPE_REAL, 'Coco')
    game = Game(player1, player2)
    print(game.checkWin(player1))
    return 0;

if __name__ == "__main__":
    main()