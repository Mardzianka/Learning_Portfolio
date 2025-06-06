#Ch 12 Example 3 hello goodbye.py
#program places label and two buttons in a window
#pressing a button changes the label text
 
from tkinter import *

def greeting():
   label.config (text = "Hello!")
   
def farewell():
   label.config (text = "Goodbye!")

#set the window parameters
window = Tk()
window.geometry('200x120')
window.title("Demo")
# window is not resizable in either direction
window.resizable (False, False) 
window.configure(background = "Light blue")

#define and place labels and buttons
label = Label(window, text = "Press a button")
label.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20)

button1 = Button(window, text = "Greeting", width = 7, command = greeting)
button1.grid(row = 1,column = 0, padx = 20)

button2 = Button(window, text = "Farewell", width = 7, command = farewell)
button2.grid(row = 1,column = 1, padx = 20)

#run mainloop
window.mainloop()

   
   

