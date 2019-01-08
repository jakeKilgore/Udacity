# -*- coding: UTF-8
from query import Query
import textwrap

__easy_question = '''The ___1___ is a weblike connection of computers, split between ___2___ and ___3___.
In general, ___2___ host files while ___3___ use internet browsers to access them. ___1___ browsers
use a protocol called ___4___ to request files from ___2___ and then use HTML to interpret these files
into a human readable format called a web page.'''
__easy_answer = ["internet", "servers", "clients", "http"]

__medium_question = '''HTML stands for Hyper ___1___ ___2___ Language. It is a type of document containing:
___1___, ___2___, ___3___, and ___4___. ___1___ is simply the information conveyed with written language.
___2___ is the grammar system used by internet browsers to group information together and display it
to the user. ___3___ are how HTML accesses other files on the server or internet such as a picture,
allowing the client's internet browser to display it on the webpage. Finally, ___4___ allow HTML to direct
the client to another webpage on the internet through clickable ___1___.'''
__medium_answer = ["text", "markup", "references", "links"]

__hard_question = '''Some HTML elements are clissified as being ___1___ while others are classified as ___2___.
The main differences is that ___1___ elements, such as ___3___, will not affect its content's position on the
webpage while ___2___ elements such as ___4___ will place the element's content on a new line and create an
invisible box around the content where other content cannot be placed.'''
__hard_answer = ["inline", "block", "span", "div"]

__valid_queries = {
    "easy": Query(__easy_question, __easy_answer),
    "medium": Query(__medium_question, __medium_answer),
    "hard": Query(__hard_question, __hard_answer),
}

def playGame():
    """Play the game.

    Play rounds at the player's difficulty level until they decide to quit.
    """

    guesses = 5

    query = getQuery()
    assert query is not None, "Invalid query."
    playRound(query, 0, guesses)
    if playAgain():
        playGame()

def getQuery():
    """Get the user's desired difficulty level.

    Return:
        query (Query): The question string and a list of the answers.
    """

    difficulty = raw_input("Enter your difficulty level (easy/medium/hard): ").lower()
    if difficulty in __valid_queries:
        query = __valid_queries[difficulty]
        return Query(query.question, query.answers)
        # New query is created for replayability reasons.
    return getQuery()

def playRound(query, blank, guesses):
    """Play one round of the game.

    Arguments:
        query (Query): The question string and a list of the answers.
        blank (int): The current blank to be filled.
        guesses (int): The number of guesses the user has remaining.
    """

    assert blank >= 0 and blank < len(query.answers), "Out of question range."
    assert guesses > 0, "Remaining guesses must be positive."

    correct = False
    while guesses > 0:
        input = getInput(query, blank, guesses)
        correct = checkAnswer(query, blank, input)
        if correct: break
        guesses -= 1
    if not correct:
        print "You are out of guesses!"
        return
    query.fillBlanks(blank)
    if blank == len(query.answers) - 1:
        print textwrap.fill(query.question)
        return
    return playRound(query, blank + 1, guesses)

def getInput(query, blank, guesses):
    """Obtain and return the user's guess at the current input.

    Arguments:
        query (list): The question string and a list of the answers.
        blank (int): The current blank to be filled.
        guesses (int): The number of guesses the user has remaining.
    """

    if guesses > 1:
        guess = " guesses "
    else:
        guess = " guess "
    print
    print textwrap.fill(query.question)
    print
    print "You have " + str(guesses) + guess + "remaining."
    return raw_input("What should replace ___" + str(blank + 1) + "___? ").lower()

def checkAnswer(query, blank, input):
    """Return whether the input matches the correct answer."""
    correct = query.checkAnswer(blank, input)
    if correct:
        print "Correct!"
    else:
        print "Wrong!"
    return correct

def playAgain():
    """Return whether the user wants to play again."""
    input = raw_input("Play again? (y/n): ").lower()
    if input == 'y':
        return True
    if input == 'n':
        return False
    return playAgain()

playGame()
