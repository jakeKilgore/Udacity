class Query:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def fillBlanks(self, blank):
        self.question = self.question.replace("___" + str(blank + 1) + "___", self.answers[blank])

    def checkAnswer(self, blank, input):
        return input == self.answers[blank]
