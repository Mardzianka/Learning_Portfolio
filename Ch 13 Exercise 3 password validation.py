#Program name: Ch 13 Exercise 3 password validation
#program to allow user to enter username and password and
# checks the password is 6 characters or more

from tkinter import *
#from tkinter import ttk
def submit(event):

    password = entry_password.get()
    username = entry_username.get()
    errorMessage = Label(root,width = 30)
    errorMessage.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
    if len(password) < 6:
        errorMessage.config(text = "Password must be at least 6 characters")
        entry_username.delete(0,'end')
        entry_password.delete(0,'end')
        entry_username.focus_set()
    else:
        errorMessage.config(text = "Password accepted")
        print("password accepted")
        print("Username: ", username)
        print("Password: ", password)

root = Tk()
root.geometry('250x200')
root.title("Login Screen")
root.resizable (False, False)
root.configure(background = "Light blue")

#place a frame round labels and user entries
frame_entry = Frame(root)
#frame_entry.pack(padx = 10, pady = 10)
frame_entry.grid(row=0,column=0,columnspan=2,padx = 10, pady = 10)

#frame_button = Frame(root)
#frame_button.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)              


#place the labels and text entry fields
Label(frame_entry, text = "Enter username: ").grid(row = 0, column = 0, padx = 5,pady = 5)

entry_username = Entry(frame_entry, width = 15, bg = "white")
entry_username.grid(row = 0, column = 1,padx = 5,pady = 5)

Label(frame_entry, text = "Enter password: ").grid(row = 1, column = 0, padx = 10, pady = 10)
# The parameter show = “*” will cause asterisks to appear in the entry box
# instead of the characters typed by the user.
entry_password = Entry(frame_entry, width = 15, bg = "white", show = "*")
entry_password.grid(row = 1, column = 1, padx = 5,pady = 5)


#place the submit button

submit_button = Button(root, text = "Submit", width = 7)
submit_button.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)
submit_button.bind('<ButtonPress>', submit)




#run mainloop
root.mainloop()
