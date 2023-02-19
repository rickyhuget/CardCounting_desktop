from deck import Deck
import tkinter as tk
import library
import random

win = tk.Tk()
win.geometry('1000x600')  # set window size
win.configure(background='dark green')

numOfDecks = 1
shoe = Deck(numOfDecks) # the "shoe" is the object that holds all the decks being used and ready to draw from
shoe.shoeStack = iter(shoe.shoeStack)
strBtn_x = 250
endBtn_x = 612

def next_card():
    global numOfIterations
    global runningCount
    if numOfIterations == -2:
        return
    if (numOfIterations < 0):
        win.after(3000)
        endCount = tk.Label(text="Running count is: " + str(runningCount//numOfDecks),
                            fg='white',
                            bg='dark green')
        endCount.place(x=400, y=250)
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

def stopDeal():
    global numOfIterations
    numOfIterations = -2
    global runningCount
    runningCount = 0
    img = tk.PhotoImage(file="card_images/PlayingCard_0_cover.GIF")
    panel.img = img  # keep a reference so it's not garbage collected
    panel['image'] = img

    btn = tk.Button(win, text='Start Deal', command=startDeal)
    btn.place(x=strBtn_x, y=300)
    btn = tk.Button(win, text='Stop Deal', command='disabled')
    btn.place(x=endBtn_x, y=300)

def startDeal():
    global numOfIterations
    #numOfIterations = random.randrange((40*numOfDecks),(50*numOfDecks))
    numOfIterations = 5
    global runningCount
    runningCount = 0

    btn = tk.Button(win, text='Start Deal', state='disabled')
    btn.place(x=strBtn_x, y=300)
    btn = tk.Button(win, text='Stop Deal', command=stopDeal)
    btn.place(x=endBtn_x, y=300)

    next_card()

panel = tk.Label(win)
panel.place(x=400, y=50)
#panel.configure(background='black')    
img = tk.PhotoImage(file="card_images/PlayingCard_0_cover.GIF")
panel.img = img  # keep a reference so it's not garbage collected
panel['image'] = img

btn = tk.Button(win, text='Start Deal', command=startDeal)
btn.place(x=strBtn_x, y=300)
btn = tk.Button(win, text='Stop Deal', state='disabled')
btn.place(x=endBtn_x, y=300)

win.mainloop()