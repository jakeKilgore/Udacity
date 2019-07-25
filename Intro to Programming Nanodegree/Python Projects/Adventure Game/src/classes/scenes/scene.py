# -*- coding: UTF-8
import time

from ..console import Console


class Scene:
    pause_time = .5

    def __init__(self, setup, proceed=True, objects=None):
        self.setup = setup
        self.proceed = proceed
        self.objects = objects if objects is not None else set()

    def play(self):
        for line in self.setup:
            if type(line) is str:
                Console.output(line, False)
            if callable(line):
                line()
        Console.end_line()
        self.action()

    def action(self):
        while not self.proceed:
            user_input = Console.user_action(objects=self.objects)
            valid_object = user_input.noun in self.objects.keys()
            valid_command = valid_object and user_input.verb in self.objects[user_input.noun].actions.keys()
            if not valid_command:
                self.invalid_command(user_input.noun, user_input.verb)
            else:
                action = self.objects[user_input.noun].actions[user_input.verb]
                assert (callable(action)), "Invalid action " + action
                self.proceed = action()

    def invalid_command(self, noun, verb):
        Console.output("Invalid command.")
        if noun is None:
            Console.output("Valid objects are:")
            for noun in self.objects:
                Console.output(noun + " ", end_line=False)
        elif verb is None:
            Console.output("Valid actions are:")
            for verb in self.objects[noun].actions:
                Console.output(verb + " ", end_line=False)
        Console.end_line()

    @staticmethod
    def pause():
        time.sleep(Scene.pause_time)
