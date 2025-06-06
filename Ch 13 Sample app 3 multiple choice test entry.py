#Program name: Ch 13 Sample app 3 multiple choice test entry.py
#program to allow entry of questions for a multiple choice test
#Questions and correct answer are printed
#and could be sent to a file for permanent storage

from tkinter import *
from tkinter import ttk

# functions executed when a button is pressed
def submit():
    if questionNumber.get() == "1":
        print("Test name", testname.get())
    print("Question number: ",questionNumber.get())
    """
    questionStem and possibleAnswers are Text widgets
    rather than Entry widgets, 
    with text going over several lines
    To retrieve the data from start to finish you need to specify the
    parameter (1.0, END) for the get() method
    """     
    print("Question stem: ",questionStem.get(1.0,END))
    print("Possible answers: ")
    print(possibleAnswers.get(1.0,END))
    print("Correct answer: ",correctAnswer.get(),"\n")
    
def clear():
#Note the difference in the parameters of the delete() method
#between clearing an Entry box and a Text box
    questionNumber.delete(0,END)
    questionStem.delete(1.0,END)
    possibleAnswers.delete(1.0,END)
    correctAnswer.delete(0,END)
    questionNumber.focus_set()

#create a fixed size window
root = Tk()
root.geometry("700x450")
root.title("Question entry")
root.resizable (False, False)
root.configure(background = "Light blue")

#place a frame to contain the form heading
frame_heading = Frame(root)
frame_heading.grid(row=0,column=0,columnspan=2,padx = 30, pady = 5)

#place a frame to contain labels and user entries
frame_entry = Frame(root)
frame_entry.grid(row=1,column=0,columnspan=2,padx = 25, pady = 10)

#place the form heading
Label(frame_heading, text = "Name of test",
      font = ('Arial',
              16)).grid(row=0,column=0,padx=0,pady=5)

#place the labels 
Label(frame_entry, text = "Enter the question number: ")\
    .grid(row=0,column=0,padx=10,pady=5, sticky = E)
Label(frame_entry, text = "Enter the stem: ")\
    .grid(row=1,column=0,padx=10,pady=5, sticky = E)
Label(frame_entry,
      text = "Enter the 3 possible answers a, b, and c: ")\
    .grid(row=2,column=0,padx=10, pady=10,sticky = NW)
Label(frame_entry, text ="Correct answer: ") \
    .grid(row=3,column=0,padx=10,pady=10, sticky = E)

#place the text entry fields
testname= Entry(frame_heading, width = 30, font = ('Arial', 16))
testname.grid(row = 0, column = 1,padx = 5,pady = 5)

questionNumber = Entry(frame_entry, width = 2, font = ('Arial', 11))
questionNumber.grid(row = 0, column = 1,padx = 5,pady = 5, sticky = W)

questionStem = Text(frame_entry, width = 50,height = 2, bg = "white", font = ('Arial', 11))
questionStem.grid(row = 1, column = 1,padx = 5,pady = 5)

possibleAnswers = Text(frame_entry, width = 50,height = 10, bg = "white", font = ('Arial', 11))
possibleAnswers.grid(row =2, column=1,padx=5,pady=5)

#You need to import ttk at the top of the program to use Combobox
correctAnswer = ttk.Combobox(frame_entry, text = "a",
                      font = ('Arial', 11))
correctAnswer.grid(row = 3, column = 1, padx = 5,pady = 5, sticky = W)
correctAnswer.config(values = ("a","b","c"))

#place the Submit  and Clear buttons
submit_button = Button(root,text="Submit",width=7,command=submit)
submit_button.grid(row=2,column=0,padx=0,pady=5)

clear_button = Button(root,text= "Clear",width=7,command=clear)
clear_button.grid(row=2,column=1,padx=0,pady=5)

#Here is where you would open a file
#ready to store the test questions and answers
print("Open the file math1.txt")

#run mainloop to draw the window and start the program running
root.mainloop()
print("carry on...")

