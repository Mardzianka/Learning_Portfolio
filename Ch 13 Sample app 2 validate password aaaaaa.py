#Program name: Ch 13 Sample app 2 validate password aaaaaa.py
#Program asks user to login, then checks password
#In this program, password is "aaaaaa"

from tkinter import *
from tkinter import messagebox

def submit():
    password = entry_password.get()
    username = entry_username.get()
    messageAlert = Label(root,width = 30)
    messageAlert.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
    if password !="aaaaaa":
        messageAlert.config(text = "Password incorrect")
        entry_username.delete(0,END)
        entry_password.delete(0,END)
        entry_username.focus_set()
        
    else:
        messageAlert.config(text = "Password accepted")
        print("password accepted")
        print("Username: ", username)
        print("Password: ", password)
        messagebox.showinfo(title = "Password OK",
                    message = "Press OK to continue")
        root.destroy()
        
# display a message box with a hint for password
def hint():
    messagebox.showinfo(title = "Password hint",
                    message = "Hint: Try password aaaaaa")
    
#create the main window
root = Tk()
root.geometry("250x180")
root.title("Login Screen")
root.resizable (False, False)
root.configure(background = "Light blue")

#place a frame round labels and user entries
frame_entry = Frame(root)
#frame_entry.pack(padx = 10, pady = 10)
frame_entry.grid(row=0,column=0,columnspan=2,padx = 10, pady = 10)

#place a frame around the buttons
frame_buttons = Frame(root)
frame_buttons.grid(row = 2, column = 0, columnspan = 3,
                   padx = 10, pady = 10)              

#place the labels and text entry fields
Label(frame_entry, text = "Enter username: ").grid(row = 0,
      column = 0, padx = 5,pady = 5)

entry_username = Entry(frame_entry, width = 15, bg = "white")
entry_username.grid(row = 0, column = 1, padx = 5, pady = 5)

Label(frame_entry, text = "Enter password: ").grid(row = 1,
      column = 0, padx = 10, pady = 10)
# The parameter show = “*” will cause asterisks to appear 
# instead of the characters typed by the user
entry_password = Entry(frame_entry, width = 15, bg = "white", show = "*")
entry_password.grid(row = 1, column = 1, padx = 5, pady = 5)

#place the submit button
submit_button = Button(frame_buttons, text = "Submit",
width = 8, command = submit)
submit_button.grid(row = 0, column = 0, padx = 5, pady = 5)

#place the Hint button
hint_button = Button(frame_buttons, text = "Password hint",
width = 15, command = hint)
hint_button.grid(row = 0, column = 1, padx = 5, pady = 5)

#run mainloop
root.mainloop()
print("carry on now...")
