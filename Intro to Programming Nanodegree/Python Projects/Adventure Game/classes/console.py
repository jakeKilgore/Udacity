# -*- coding: UTF-8
import time
import random
import shutil

from .command import Command

character_delay_range = (0.01, 0.05)    # The random time range in seconds to pause between each character.
word_delay_range = (.05, .1)            # The random time range in seconds to pause between each word.
do_character_delay = False              # Whether to pause between characters.
do_word_delay = False                   # Whether to pause between words.
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
            character_delay()
        print(' ', end='')
        current_character += 1
        word_delay()
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


def character_delay():
    """Delay the console output after each character."""
    if not do_character_delay:
        return
    time.sleep(random.uniform(*character_delay_range))


def word_delay():
    """Delay the console output after each word."""
    if not do_word_delay:
        return
    time.sleep(random.uniform(*word_delay_range))


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
