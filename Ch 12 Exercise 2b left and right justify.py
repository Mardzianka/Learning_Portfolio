#Ch 12 Exercise 2b left and right justify.py
#program places label and 2 buttons in a window
#pressing a button changes the label text
#and justifies it left or right
#In this version the window parameters are set 
from tkinter import *
 
window = Tk()
window.geometry('200x120')
window.title("Demo")
window.resizable (False, False) # not resizable in either direction
window.configure(background = "Light green")

def leftJustify():
   label.config (text = "left")
   label.grid(row = 1, column = 0, columnspan = 2,
              padx = 30, pady = 10, sticky = W)

def rightJustify():
   label.config (text = "Right")
   label.grid(row = 1, column = 0, columnspan = 2,
              padx = 30, pady = 10, sticky = E)

button1 = Button(window, text = "Left", width = 7, command = leftJustify)
button1.grid(row = 0,column = 0, padx = 20,pady = 20)

button2 = Button(window, text = "Right", width = 7, command = rightJustify)
button2.grid(row = 0,column = 1, padx = 20,pady = 20)

label = Label(window)

#run mainloop
window.mainloop()
