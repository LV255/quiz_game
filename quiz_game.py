import random
import time

time1 = 1
time2 = 2

# questions entered as a string, Question first, then the correct answer, then 3 incorrect answers.
# pay attention to commas as it makes a big impact
# correct input formula is (question?, correct answer, incorrect1, incorrect2, incorrect3)
easy_questions = ("""What is the capital of China?, Beijing, Tokyo, Hong Kong, Shanghai
Who was the first man to land on the moon?, Neil Armstrong, Buzz Aldrin, Yuri Gagarin, Michael Collins
Who was the first US president?, George Washington, Abraham Lincoln, Ronald Reagan, James A. Garfield
How many legs does a spider have?, 8, 6, 10, 2""")

medium_questions = ("""What is the capital of Korea?, Seoul, Tokyo, Osaka, Hong Kong
Who discovered penicillin?, Alexander Fleming, Albert Einstein, Marie Curie, Isaac Newton
Which has most calories per gram?, fat, protein, carbohydrate, fiber
Which city is furthest North?, Glasgow, Manchester, Berlin, Beijing""")

hard_questions = ("""What is the capital of Japan?, Tokyo, Shanghai, Osaka, Taipei
Who discovered Jupiter?, Galileo Galilei, Nicolaus Copernicus, Nicolaus Copernicus, Edwin Hubble
How many McDonald's restaurants are there in the UK?, 1300, 500, 2000, 300
Where does the Queen live?, Buckingham palace, Downing street, The mall, Nottingham castle""")


# turn the multiple q string above into a list, each list item is one Q and A
easy_q_to_list = easy_questions.split("\n")
medium_q_to_list = medium_questions.split("\n")
hard_q_to_list = hard_questions.split("\n")

# keep track of progress
questions_right = 0
progress_bar = "Progress bar: "

def ask_a_question():

    # allow function to modify progress info
    global questions_right
    global progress_bar

    # allow function to modify list if we reset the game
    global easy_q_to_list
    global medium_q_to_list
    global hard_q_to_list

    # print progress information and first question
    if questions_right > 0:
        time.sleep(time1)
        print()
        print("Number of correct answers: " + str(questions_right))
        print(progress_bar)
        time.sleep(time2)

    # decide to ask easy, medium or hard
    level_to_ask = None
    if questions_right < 3:
        level_to_ask = easy_q_to_list
    elif questions_right >= 3 and questions_right < 6:
        level_to_ask = medium_q_to_list
    elif questions_right >= 6 and questions_right < 9:
        level_to_ask = hard_q_to_list

    # randomly select a question from the list
    # select random number from list that decreases as list length goes down
    # remember minus one as index starts at 0, len doesnt.
    random_q_number = random.randint(0, (len(level_to_ask) - 1))

    # turn a randomly selected q into a list, each item is Q and then 4 answers
    split_q_1 = level_to_ask[random_q_number].split(",")

    # take the correct answer and save it as a variable, and strip it of whitespace too
    correct_answer = split_q_1[1].strip()

    # get four random numbers to randomly assign the answers to
    option_list = [1, 2, 3, 4]
    random_choice1 = random.choice(option_list)
    option_list.remove(random_choice1)

    random_choice2 = random.choice(option_list)
    option_list.remove(random_choice2)

    random_choice3 = random.choice(option_list)
    option_list.remove(random_choice3)

    random_choice4 = random.choice(option_list)
    option_list.remove(random_choice4)

    # print question
    print()
    if questions_right < 8:
        print("Question " + str(questions_right + 1))
    else:
        print("Final Question!" )
    time.sleep(time2)
    print()
    print(split_q_1[0])
    time.sleep(time2)

    # print random answers
    print("A:" + split_q_1[random_choice1] + "   B:" + split_q_1[random_choice2] + "   C:" + split_q_1[random_choice3] + "   D:" + split_q_1[random_choice4])

    # find the correct answer amongst the random answers and save it to a variable
    answer_to_check = ""

    if split_q_1[random_choice1].strip() == correct_answer:
        answer_to_check = "a"
    elif split_q_1[random_choice2].strip() == correct_answer:
        answer_to_check = "b"
    elif split_q_1[random_choice3].strip() == correct_answer:
        answer_to_check = "c"
    elif split_q_1[random_choice4].strip() == correct_answer:
        answer_to_check = "d"

    # ask for the answer
    # reply with various answers
    time.sleep(time1)
    print()
    player_answer = input("Select correct answer (a/b/c/d): ").strip().lower()
    if player_answer == answer_to_check:
        time.sleep(time1)
        print()
        varied_answer_list = ["Well done, that's correct!", "That's the right answer.", "You got it! Well done.", "Correct.",
                              "That's right!", "Great answer!", "Yes, that's right.", "Yes, that's correct."]
        print(varied_answer_list[random.randint(0, len(varied_answer_list) - 1)])
        time.sleep(time2)

        #remove the used question from the list of questions
        level_to_ask.pop(random_q_number)

        # add a gap so we can see changes in levels to progress bar
        if (questions_right == 3) or (questions_right == 6):
            progress_bar += " "

        #add a tick to the progress bar
        progress_bar += "|"

        # add to the questions right tally
        questions_right += 1

        # print(len(level_to_ask))
        if questions_right == 9:
            print()
            time.sleep(time1)
            print("Correctly answers questions: " + str(questions_right))
            print(progress_bar)
            time.sleep(time1)
            print()
            print("Well done you got all 9 questions right!")
            time.sleep(time2)
            print()
            play_again = input("Do you want to play again? (y/n) ").strip().lower()
            if play_again == "y":
                time.sleep(time1)
                ask_a_question()

        # if not ask the next question
        else:
            ask_a_question()
    else:
        time.sleep(time1)
        print()
        print("Sorry, you failed!")

        # reset progress bars
        questions_right = 0
        progress_bar = "Progress bar: "

        # add things back into lists.
        easy_q_to_list = easy_questions.split("\n")
        medium_q_to_list = medium_questions.split("\n")
        hard_q_to_list = hard_questions.split("\n")

        # play again
        time.sleep(time1)
        print()
        play_again = input("Do you want to play again? (y/n) ").strip().lower()
        if play_again == "y":
            time.sleep(time1)
            ask_a_question()

def start():
    print("  ***  Welcome to the quiz  ***  ")
    time.sleep(time1)
    print("If you can answer 9 questions in a row you win!")
    time.sleep(time1)
    print("The questions will get harder as you go along.")
    time.sleep(time1)
    begin = input("Are you ready to being? (type y/n and press enter) ")
    if begin == "y":
        time.sleep(time1)
        ask_a_question()
    else:
        time.sleep(time1)
        print()
        start()

start()



