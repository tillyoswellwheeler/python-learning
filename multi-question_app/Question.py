#--------------------------------------------
# Python Learning -- Multi-Question Class App
#--------------------------------------------

#-------------------------------------
# Modelling a question and creating a Question Data type


class Question:

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer