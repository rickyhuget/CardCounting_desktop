from deck import Deck
import tkinter as tk
#from PIL import ImageTk, Image
import random
import library

win = tk.Tk()
win.geometry('1000x600')  # set window size
#win.resizable(0, 0)  # fix window

global numOfIterations
numOfIterations = random.randrange(40,50)
#numOfIterations = 3
global runningCount
runningCount = 0

panel = tk.Label(win)
panel.pack()

numOfDecks = 1
shoe = Deck(numOfDecks) # the "shoe" is the object that holds all the decks being used and ready to draw from
shoe.shoeStack = iter(shoe.shoeStack)

def next_card():
    global numOfIterations
    global runningCount
    if (numOfIterations < 0):
        win.after(3000)
        endCount = tk.Label(text="Running count is: " + str(runningCount))
        endCount.pack()
        return
    try:
        card = next(shoe.shoeStack)  # get the next image from the iterator
    except StopIteration:
        return  # if there are no more images, do nothing

    if (library.numberCard(card.value)):
        runningCount += 1
    if (library.faceCard(card.value)):
        runningCount -= 1
    
    print(numOfIterations+1, card.value, card.suit, runningCount)
    numOfIterations -= 1
    img = card.image
    panel.img = img  # keep a reference so it's not garbage collected
    panel['image'] = img
    win.after(1000, next_card)

def startDeal():
    btn = tk.Button(win, text='Start Deal', state='disabled')
    btn.place(x=450, y=300)
    global runningCount
    runningCount = 0
    next_card()
    
btn = tk.Button(win, text='Start Deal', command=startDeal)
btn.place(x=450, y=300)

win.mainloop()