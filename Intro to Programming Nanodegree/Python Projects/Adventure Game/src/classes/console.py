# -*- coding: UTF-8
import time
import random
from ..classes import vocabulary
from .action import Action


class Console:
    character_limit = 120
    current_character = 0

    @staticmethod
    def output(output, end_line=True):
        words = str(output).split(' ')
        for word in words:
            if len(word) > Console.character_limit - Console.current_character:
                Console.end_line()
            for character in word:
                print(character, end='')
                Console.current_character += 1
                #Console.character_delay()
            print(' ', end='')
            Console.current_character += 1
            Console.word_delay()
        if end_line:
            Console.end_line()

    @staticmethod
    def whitespace(num_lines=1):
        for _ in range(num_lines):
            Console.end_line()

    @staticmethod
    def end_line():
        print()
        Console.current_character = 0

    @staticmethod
    def character_delay():
        time.sleep(random.uniform(0.01, 0.05))

    @staticmethod
    def word_delay():
        time.sleep(random.uniform(.1, .3))

    @staticmethod
    def user_action(nouns=None, verbs=None):
        if nouns is None:
            nouns = []
        if verbs is None:
            verbs = []
        noun = None
        verb = None
        user_input = input().split(' ')
        for word in user_input:
            word = Console.format(word)
            if word in nouns or word in vocabulary.nouns_list:
                noun = word
            if word in verbs or word in vocabulary.verbs_list:
                verb = word
        return Action(verb, noun)

    @staticmethod
    def format(string):
        if len(string) > 1:
            return string[0].upper() + string[1:].lower()
        else:
            return string.upper()
