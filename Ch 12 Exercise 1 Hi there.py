# Ch 12 Exercise 1 Hi there
from tkinter import *
window = Tk()
window.title("Placing a button")

def clickButton():
  showText = Label(window, text = "Hi there!")
  showText.pack()
  
button = Button(window, text = "Click here", command = clickButton)
button.pack()

window.mainloop()
