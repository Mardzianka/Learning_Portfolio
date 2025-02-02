""" This program will display a question and answer to the user
    and allow the user to navigate through the questions and answers
    using the keyboard. The user can also see the number of questions
    and answers, see a random question and answer, see the first and
    last question and answer, see the previous and next question and
    answer, see the question and answer number, and see the question
    and answer. The user can exit the program by pressing the escape
    key. """

# import the sys module
import sys

# import the random module
import random

# define the main function
def main():
    """
    Main function to run the flashcard program.
    This function reads questions and answers from a file, shuffles them, and
    allows the user to navigate through the questions and answers using various
    key inputs.
    Key Inputs:
    - " ": Show the next answer.
    - "\r": Show the next question.
    - "\x1b": Exit the program.
    - "\x08": Show the previous question.
    - "\x1b[H": Show the first question.
    - "\x1b[F": Show the last question.
    - "r": Show a random question.
    - "q": Show the current question.
    - "a": Show the current answer.
    - "n": Show the number of questions.
    - "m": Show the number of answers.
    - "f": Show the first answer.
    - "l": Show the last answer.
    - "p": Show the previous answer.
    - "o": Show the next answer.
    - "t": Show a random answer.
    - "z": Show the current question and answer.
    - "x": Show the current question and answer number.
    The function ensures that the number of questions and answers match and
    exits if there are no questions or answers.
    """
    # open the file and read the lines

    with open("AIgeneratedQ&Afor_flashcards.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        questions = []
        answers = []
        for line in lines:
            if line.strip() == "Question:":
                questions.append("")
            elif line.strip() == "Answer:":
                answers.append("")
            elif len(questions) == len(answers):
                questions[-1] += line
            else:
                answers[-1] += line

    # create a list of indexes for the questions and answers

    question_indexes = list(range(len(questions)))
    answer_indexes = list(range(len(answers)))

    # set the current question and answer to 0

    current_question = 0
    current_answer = 0

    # check if the number of questions and answers match

    if len(questions) != len(answers):
        print("The number of questions and answers do not match")
        sys.exit()

    # check if there are any questions and answers

    if len(questions) == 0:
        print("There are no questions or answers")
        sys.exit()

    # shuffle the questions and answers

    random.shuffle(question_indexes)
    random.shuffle(answer_indexes)

    # display the first question and answer

    print("Question 1: " + questions[question_indexes[current_question]])
    print("Answer 1: " + answers[answer_indexes[current_answer]])

    # loop until the user exits the program

    while True:        # get a key from the user

        key = input("Press a key: ")

        # check if the user wants to see the answer

        if key == " ":
            current_answer += 1
            if current_answer == len(answers):
                current_answer = 0
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])

        # check if the user wants to see the next question

        elif key == "\r":
            current_question += 1
            if current_question == len(questions):
                current_question = 0
            print("Question " + str(current_question + 1) + ": "
                  + questions[question_indexes[current_question]])

        # check if the user wants to exit the program

        elif key == "\x1b":
            break

        # check if the user wants to see the previous question
        elif key == "\x08":
            current_question -= 1
            if current_question == -1:
                current_question = len(questions) - 1
            print("Question " + str(current_question + 1) + ": "
                  + questions[question_indexes[current_question]])

        # check if the user wants to see the first question

        elif key == "\x1b[H":
            current_question = 0
            print("Question " + str(current_question + 1) + ": "
                  + questions[question_indexes[current_question]])

        # check if the user wants to see the last question

        elif key == "\x1b[F":
            current_question = len(questions) - 1
            print("Question " + str(current_question + 1) + ": "
                  + questions[question_indexes[current_question]])

        # check if the user wants to see a random question

        elif key == "r":
            current_question = random.randint(0, len(questions) - 1)
            print("Question " + str(current_question + 1) + ": "
                  + questions[question_indexes[current_question]])

        # check if the user wants to see the question number

        elif key == "q":
            print("Question " + str(current_question + 1) + ": "
                  + questions[question_indexes[current_question]])

        # check if the user wants to see the answer number

        elif key == "a":
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])

        # check if the user wants to see the number of

        elif key == "n":
            print("Number of questions: " + str(len(questions)))

        # check if the user wants to see the number of answers
        elif key == "m":
            print("Number of answers: " + str(len(answers)))

        # check if the user wants to see the first answer
        elif key == "f":
            current_answer = 0
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])

        # check if the user wants to see the last answer
        elif key == "l":
            current_answer = len(answers) - 1
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])

        # check if the user wants to see the previous answer
        elif key == "p":
            current_answer -= 1
            if current_answer == -1:
                current_answer = len(answers) - 1
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])

        # check if the user wants to see the next answer
        elif key == "o":
            current_answer += 1
            if current_answer == len(answers):
                current_answer = 0
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])

        # check if the user wants to see a random answer
        elif key == "t":
            current_answer = random.randint(0, len(answers) - 1)
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])

        # check if the user wants to see the question and answer

        elif key == "z":
            print("Question " + str(current_question + 1) + ": "
                  + questions[question_indexes[current_question]])
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])

        # check if the user wants to see the question and answer number
        elif key == "x":
            print("Question " + str(current_question + 1) + ": "
                  + questions[question_indexes[current_question]])
            print("Answer " + str(current_answer + 1) + ": "
                  + answers[answer_indexes[current_answer]])
if __name__ == "__main__":
    main()

# End of program
