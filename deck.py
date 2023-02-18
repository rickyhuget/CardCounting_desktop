from card import createShuffledCardStack

class Deck():
  def __init__(self, numOfDecks):
    self.shoeStack = createShuffledCardStack(numOfDecks)
    self.runningCount = 0