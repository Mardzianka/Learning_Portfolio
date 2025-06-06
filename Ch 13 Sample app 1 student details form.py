#Program name: Ch 13 Sample app 1 student details form.py
#program to allow entry of user ID, surname and first name 
from tkinter import *

# functions executed when a button is pressed
def submit():
    print("Username",username.get())
    print("First name",firstname.get())
    print("Surname",surname.get())
    
def clear():
    username.delete(0,END)
    firstname.delete(0,END)
    surname.delete(0,END)
    username.focus_set()

#create a fixed size window
root = Tk()
root.geometry("270x240")
root.title("Student details")
root.resizable (False, False)
root.configure(background = "Light blue")

#place a frame to contain the form heading
frame_heading = Frame(root)
frame_heading.grid(row=0,column=0,columnspan=2,padx = 30, pady = 5)

#place a frame to contain labels and user entries
frame_entry = Frame(root)
frame_entry.grid(row=1,column=0,columnspan=2,padx = 25, pady = 10)

#place the form heading
Label(frame_heading, text = "Student details form",
font = ('Arial', 16))\
        .grid(row=0,column=0,padx=0,pady=5)

#place the labels 
Label(frame_entry, text = "Username: ")\
        .grid(row=0, column=0, padx=10, pady=5)
Label(frame_entry, text = "First name: ")\
        .grid(row=1, column=0, padx=10, pady=10)
Label(frame_entry, text = "Surname: ")\
        .grid(row=2, column=0, padx=10, pady=10)

#place the text entry fields
username = Entry(frame_entry, width = 15, bg = "white")
username.grid(row=0, column=1, padx=5, pady=5)

firstname = Entry(frame_entry, width = 15, bg = "white")
firstname.grid(row=1, column=1, padx=5, pady=5)

surname = Entry(frame_entry, width = 15, bg = "white")
surname.grid(row=2, column=1, padx=5, pady=5)

#place the Submit  and Clear buttons
submit_button = Button(root,text="Submit",width=7, command = submit)
submit_button.grid(row=2, column=0, padx=0, pady=5)


clear_button = Button(root,text= "Clear",width=7,command=clear)
clear_button.grid(row=2, column=1, padx=0, pady=5)

#run mainloop to draw the window and start the program running
root.mainloop()
