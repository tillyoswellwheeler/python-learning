#--------------------------------------------
# Python Learning -- Multi-Question Class App
#--------------------------------------------

from Question import Question
#-------------------------------------
# Creating Question Object and App

question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple/Red\n(c) Grey\n\n",
    "What colour are Bananas?\n(a) Teal/Green\n(b) Magenta/Red\n(c) Yellow\n\n",
    "What colour are Cherries?\n(a) Red/Green\n(b) Purple/Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def ask_questions(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer is question.answer:
            score += 1
        else:
            "Invalid choice"
    print("You got {} Correct".format(score))

ask_questions(questions)