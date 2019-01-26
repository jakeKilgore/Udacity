# -*- coding: UTF-8
class Query:
    """Class for handling the levels in the quiz.

    Attributes:
        question (str): String with blanks to be filled in by guessing the
                        answers.
        answers (List[str]): List of answers used to fill in the blanks in the
                             question.
    """

    def __init__(self, question, answers):
        """Constructor for the Query class.

        Parameters:
            question (str): String with blanks to be filled in by guessing the
                            answers.
            answers (List[str]): List of answers used to fill in the blanks in
                                 the question.
        """
        self.question = question
        self.answers = answers

    def fill_blanks(self, blank):
        """Replace the given blank in the question with its associated answer.

        Parameters:
            blank (int): Number indicating which blank to replace.
        """
        self.question = self.question.replace(
            "___" + str(blank + 1) + "___", self.answers[blank])

    def check_answer(self, blank, user_input):
        """Check if the user's input matches the given answer.

        Parameters:
            blank (int): Number indicating the current answer.
            user_input (str): The user's input.

        Return:
            boolean: True if the input matches the answer, false otherwise.
        """
        return user_input == self.answers[blank]
