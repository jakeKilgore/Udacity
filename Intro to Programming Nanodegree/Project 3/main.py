from query import Query

__sample_question = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
__sample_answer = ["test", "test", "test", "test"]

__valid_queries = {
    "easy": Query(__sample_question, __sample_answer),
    "medium": Query(__sample_question, __sample_answer),
    "hard": Query(__sample_question, __sample_answer),
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
        print query.question
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
    print query.question
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
