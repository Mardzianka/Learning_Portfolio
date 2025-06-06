#Program name: Ch 13 Exercise 4 Write test to file.py
#program to allow entry of questions for a multiple choice test
#Questions and correct answer are sent to a file for permanent storage

from tkinter import *
from tkinter import ttk

#write testname to file
def storeTestName(newTestName):
    global testFile
    testFile.write(newTestName + "\n")

#write data to text file
def storeQuestion(nextLine):
    global testFile
    testFile.write(nextLine + "\n")
          
# functions executed when a button is pressed
def submit():
    question1 = questionNumber.get()
    if question1 == "1":
        newTestName = testname.get()
        storeTestName(newTestName)
    newQuestionNumber = questionNumber.get()
    storeQuestion(newQuestionNumber)
    
    newQuestionStem = questionStem.get(1.0,END)
    storeQuestion(newQuestionStem)
    
    newAnswers = question.get(1.0,END)
    storeQuestion(newAnswers)
    
    newCorrectAnswer = answer.get()
    storeQuestion(newCorrectAnswer)     
    
def clear():
    questionNumber.delete(0,END)
    questionStem.delete(1.0,END)
    question.delete(1.0,END)
    answer.delete(0,END)
    questionNumber.focus_set()

#create a fixed size window
root = Tk()
root.geometry("700x450")
root.title("Question entry")
root.resizable (False, False)
root.configure(background = "Light blue")

#place a frame to contain the form heading
frame_heading = Frame(root)
frame_heading.grid(row=0, column=0, columnspan=2,padx = 30, pady = 5)

#place a frame to contain labels and user entries
frame_entry = Frame(root)
frame_entry.grid(row=1, column=0, columnspan=2, padx = 25, pady = 10)

#place the form heading
Label(frame_heading, text = "Name of test", font = ('Arial', 16))\
        .grid(row=0, column=0, padx=0, pady=5)

#place the labels 
Label(frame_entry, text = "Enter the question number: ")\
        .grid(row=0, column=0, padx=10, pady=5, sticky = E)
Label(frame_entry, text = "Enter the stem: ")\
        .grid(row=1, column=0, padx=10, pady=5, sticky = E)
Label(frame_entry, text = "Enter the 3 possible answers a, b, and c: ")\
        .grid(row=2,column=0, padx=10, pady=10, sticky = NW)
Label(frame_entry, text ="Correct answer: ") \
        .grid(row=3,column=0, padx=10, pady=10, sticky = E)

#place the text entry fields
testname= Entry(frame_heading, width = 30, font = ('Arial', 16))
testname.grid(row = 0, column = 1,padx = 5,pady = 5)

questionNumber = Entry(frame_entry, width = 2, font = ('Arial', 11))
questionNumber.grid(row = 0, column = 1,padx = 5,pady = 5, sticky = W)

questionStem = Text(frame_entry, width = 50,height = 2, bg = "white", \
                    font = ('Arial', 11))
questionStem.grid(row = 1, column = 1,padx = 5, pady = 5)

question = Text(frame_entry, width = 50,height = 10, bg = "white", \
                font = ('Arial', 11))
question.grid(row =2, column=1, padx=5, pady=5)

#You need to import ttk at the top of the program to use Combobox
answer = ttk.Combobox(frame_entry, text = "a", font = ('Arial', 11))
answer.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)
answer.config(values = ("a","b","c"))

#place the Submit and Clear buttons
submit_button = Button(root,text="Submit",width=7,command=submit)
submit_button.grid(row=2, column=0, padx=0, pady=5)

clear_button = Button(root,text= "Clear",width=7,command=clear)
clear_button.grid(row=2, column=1, padx=0, pady=5)


#main program starts here
print ("The data entry window will open automatically")
print("If you can't see it, look behind the other windows on your screen")
print("Do not press Enter after entering the test name or the question stem")
print("Use the mouse to go to the next field")
print("\nDo not leave blank lines between the answers or after the last answer")
fileName = input("Enter a name for the text file with extension .txt: ")
testFile = open(fileName,"w")
#run mainloop to draw the window and allow data entry
root.mainloop()

testFile.close()   
print("Goodbye") 
