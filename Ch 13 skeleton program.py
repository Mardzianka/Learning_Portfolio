#Program name: Ch 13 skeleton program.py
#program to allow entry of user ID, surname and first name 
from tkinter import *

# function executed when Submit button is pressed
def submit():
    print("Username",username.get())
    print("First name",firstname.get())
    print("Surname",surname.get())
    
# function executed when Clear button is pressed  
def clear():
    username.delete(0,END)
    firstname.delete(0,END)
    surname.delete(0,END)
    username.focus_set()

#create a fixed size window
root = Tk()

#place a frame to contain the form heading

#place a frame to contain labels and user entries

#place the form heading

#place the labels 

#place the text entry fields

#place the Submit  and Clear buttons

#run mainloop to draw the window and start the program running
root.mainloop()
