from xmlrpc.client import Boolean


PLAYER_TYPE_AI = 'AI'
PLAYER_TYPE_REAL = 'REAL'

class Player:
  
  # Type of the player: AI or REAL  
  type = ''
  
  # Name of the player
  name = 'Unknow'
  
  # The symbol use on the grid
  character = ''
  
  # Indicate if it's this player turn in the game
  turn_to_play = False

  def __init__(self, type, name):
      if (type not in [PLAYER_TYPE_AI, PLAYER_TYPE_REAL]):
          return 84
      
      self.type = type
      self.name = name
      self.turn_to_play = False
  
  def getType(self):
      return self.type
  
  def setType(self, type):
      self.type = type
  
  def getName(self):
      return self.name
  
  def setName(self, name):
      self.name = name
  
  def getCharacter(self):
      return self.character
  
  def setCharacter(self, character):
      self.character = character
  
  def setTurnToPlay(self, turn_to_play):
      self.turn_to_play = turn_to_play