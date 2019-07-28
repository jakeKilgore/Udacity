# -*- coding: UTF-8
class Command:
    """Class handling the structure of user commands.

    Attributes:
        verb (str): The action of the command.
        noun (str): The object of the command.
    """
    def __init__(self, verb, noun):
        """Constructor for the Command class.

        Parameters:
            verb (str): The action of the command.
            noun (str): The object of the command.
        """
        self.verb = verb
        self.noun = noun
