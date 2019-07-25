# -*- coding: UTF-8
import time
import random

from .action import Action

character_delay_range = (0.01, 0.05)
word_delay_range = (.1, .3)
character_delay = False
word_delay = False


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
                if character is '\n':
                    Console.end_line()
                    continue
                print(character, end='')
                Console.current_character += 1
                Console.character_delay()
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
        if not character_delay:
            return
        time.sleep(random.uniform(*character_delay_range))

    @staticmethod
    def word_delay():
        if not word_delay:
            return
        time.sleep(random.uniform(*word_delay_range))

    @staticmethod
    def user_action(objects=None, noun=None, verb=None):
        if objects is None:
            objects = {}
        actions = set()
        for obj in objects.keys():
            actions.update(objects[obj].actions.keys())
        user_input = input().split(' ')
        for word in user_input:
            word = Console.format(word)
            if word in objects.keys():
                noun = word
            if word in actions:
                verb = word
        return Action(verb, noun)

    @staticmethod
    def format(string):
        if len(string) > 1:
            return string[0].upper() + string[1:].lower()
        else:
            return string.upper()
