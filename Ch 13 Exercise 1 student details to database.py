#Program name: Ch 13 Exercise 1 student details to database.py
#program to allow entry of user ID, surname and first name
#and store them in a new database
from tkinter import *
import sqlite3

conn = sqlite3.connect("studentinfo.db")
cursor = conn.cursor()



# functions executed when a button is pressed
def submit():
    aUserName = username.get()
    aFirstName = firstname.get()
    aSurname = surname.get()

    myRec = []
    myRec.append(aUserName)
    myRec.append(aFirstName)
    myRec.append(aSurname)
    cursor.execute("INSERT INTO tblStudent VALUES (?,?,?)",myRec)
    conn.commit()
                   
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
Label(frame_heading, text = "Student details form", font = ('Arial', 16))\
        .grid(row=0,column=0,padx=0,pady=5)

#place the labels 
Label(frame_entry, text = "Username: ")\
        .grid(row=0, column=0, padx=10, pady=5)
Label(frame_entry, text = "First name: ")\
        .grid(row=1, column=0, padx=10, pady=10)
Label(frame_entry, text ="Surname: ") \
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

def createNewTable():
    print ("The details will be saved to a database studentinfo.db")
    sqlCommand = """
        CREATE TABLE tblStudent
        (
        userName string,
        firstname string,
        surname string,
        primary key (username)
        )"""
    cursor.execute(sqlCommand)
    print("\ntblStudent created in studentinfo.db")
    conn.commit()

#main program
#create database table if it does not already exist
newTable = input ("Create new database (Y or N)? ")
if newTable.upper() == "Y":
    createNewTable()
    
#run mainloop to draw the window and start the program running
root.mainloop()
conn.close()
print("File closed")
