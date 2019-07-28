# -*- coding: UTF-8
import time
import random
import shutil

from .command import Command

character_delay_range = (0.01, 0.05)    # The random time range in seconds to pause between each character.
word_delay_range = (.05, .1)            # The random time range in seconds to pause between each word.
comma_delay_time = .3                   # The time in seconds to pause after a comma.
sentence_delay_time = .5                # The time in seconds to pause between sentences.
do_delay = True                         # Whether to slow down console output.
current_character = 0                   # Current place on the line.


def output(string_output, new_line=True):
    """Output a string of text to the console.

    The string will be typed out character-by-character, with an optional delay between the characters and the
    words. The function will also keep text to the character limit on each line.
    """
    character_limit = shutil.get_terminal_size()[0]   # The character limit on each line of the console.
    global current_character
    words = str(string_output).split(' ')
    for word in words:
        if len(word) >= character_limit - current_character:
            end_line()
        for character in word:
            if character is '\n':
                end_line()
                continue
            print(character, end='', flush=True)
            current_character += 1
            if do_delay:
                delay(character_delay_range)
                if character is '.':
                    delay(sentence_delay_time)
                elif character is ',':
                    delay(comma_delay_time)
        print(' ', end='')
        current_character += 1
        if do_delay:
            delay(word_delay_range)
    if new_line:
        end_line()


def whitespace(num_lines=1):
    """Create a set number of empty lines."""
    for _ in range(num_lines):
        end_line()


def end_line():
    """End the current line and reset the current_character counter."""
    print()
    global current_character
    current_character = 0


def delay(delay_time):
    """Delay the console output for a moment."""
    if type(delay_time) is tuple:
        time.sleep(random.uniform(*delay_time))
    else:
        time.sleep(delay_time)


def user_action(objects=None, noun=None, verb=None):
    """Accept user input and parse it into a command."""
    if objects is None:
        objects = {}
    actions = set()
    for obj in objects.keys():
        actions.update(objects[obj].actions.keys())
    user_input = input().split(' ')
    for word in user_input:
        word = word.lower()
        if word in objects.keys():
            noun = word
        if word in actions:
            verb = word
    return Command(verb, noun)
