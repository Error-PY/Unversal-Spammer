import keyboard
import time
import tkinter as tk
from tkinter import *
import os
import time
import keyboard

Version = "1.1"


triggered = 0

root = Tk()
root.title("Universal-Spammer")

version = Label(root,text="Version: "+ Version)
version.pack()

logo = Label(root,height=10,width=50,text="")
logo.pack()

canvas = Canvas(root, width = 120, height = 100)
canvas.pack()
img = PhotoImage(file="maxresdefault.ppm")
canvas.create_image(20,20, anchor=NW, image=img)

credits= Label(root,text="Made by Error_404#3059")
credits.pack()

e_info = Label(root,text="What to Spam?")
e_info.pack()
e = Entry(root, width=50, bg="grey", fg="black")
e.pack()
e.get()
howMuch_info = Label(root,text="How much to spam?")
howMuch_info.pack()
howMuch= Entry(root,width=50,bg="grey",fg="black")
howMuch.pack()


def myClick():
    time.sleep(5)
    print(howMuch.get())
    x = 0
    while (x < int(howMuch.get())):
        keyboard.write(e.get())
        keyboard.press_and_release('enter')
        x = x + 1

def antiLag():
    time.sleep(5)
    print(howMuch.get())
    x = 0
    while (x < int(howMuch.get())):
        keyboard.write(e.get())
        keyboard.press_and_release('enter')
        time.sleep(0.1)
        x = x + 1


myButton = Button(root, text="Start Spamming! (Starting in 5 Seconds)", command=myClick)
myButton.pack()


antilag_myButton = Button(root, text="Start Spamming! (Anti-Lag)", command=antiLag)
antilag_myButton.pack()

root.mainloop()


