import tkinter
import random

def createCardStack(numOfDecks):
  cardStack = []
  x = range(numOfDecks)
  for n in x:
    for value in range(2, 10):
        # ASCII value used by adding 48 and converting to char
        # value and suit are used to identify appropriate image in file 'card_images'
        cardStack.append(Card(chr(value+48), 'S', "card_images/PlayingCard_" + chr(value+48) + 'S' + ".GIF"))
        cardStack.append(Card(chr(value+48), 'H', "card_images/PlayingCard_" + chr(value+48) + 'H' + ".GIF"))
        cardStack.append(Card(chr(value+48), 'D', "card_images/PlayingCard_" + chr(value+48) + 'D' + ".GIF"))
        cardStack.append(Card(chr(value+48), 'C', "card_images/PlayingCard_" + chr(value+48) + 'C' + ".GIF"))
    faceCards = ['T', 'J', 'Q', 'K', 'A'] # value of 10 is included in faceCards[] as 'T'
    for value in faceCards:
        # value and suit are used to identify appropriate image in file 'card_images'
        cardStack.append(Card(value, 'S', "card_images/PlayingCard_" + value + 'S' + ".GIF"))
        cardStack.append(Card(value, 'H', "card_images/PlayingCard_" + value + 'H' + ".GIF"))
        cardStack.append(Card(value, 'D', "card_images/PlayingCard_" + value + 'D' + ".GIF"))
        cardStack.append(Card(value, 'C', "card_images/PlayingCard_" + value + 'C' + ".GIF"))
  return cardStack

def createShuffledCardStack(numOfDecks):
  shoeStack = createCardStack(numOfDecks)
  random.shuffle(shoeStack)
  return shoeStack

class Card():
  def __init__(self, v, s, img):
    self.value = v
    self.suit = s
    self.image = tkinter.PhotoImage(file=img)