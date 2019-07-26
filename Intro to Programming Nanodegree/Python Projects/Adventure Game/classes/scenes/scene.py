# -*- coding: UTF-8
import time

import classes.console as console


class Scene:
    """Class for handling scenes in the game.

    Scenes begin with a setup and then either proceed or move into the action.

    Attributes:
        setup (list[str or lambda]): A list of strings or function calls to make in order to introduce the scene.
        proceed (bool): Whether or not the scene should end at the end of the setup.
        objects (dict[Interactable]): A collection of items in the scene.
    """

    pause_time = .5     # The time in seconds to delay the scene during pauses.

    def __init__(self, setup, proceed=True, objects=None):
        """Constructor for the Scene class.

        Parameters:
            setup (list[str or lambda]): A list of strings or function calls to make in order to introduce the scene.
            proceed (bool): Whether or not the scene should end at the end of the setup. Defaults to True.
            objects (dict[Interactable]): A collection of items in the scene. Defaults to an empty set.
        """
        self.setup = setup
        self.proceed = proceed
        self.objects = objects if objects is not None else dict()

    def play(self):
        """Play the setup of the scene.

        The method will go line by line of the setup list, either printing out the string to the console or making
        function calls.
        """
        for line in self.setup:
            if type(line) is str:
                console.output(line, False)
            if callable(line):
                line()
        console.end_line()
        self.action()

    def action(self):
        """If the scene is not set to proceed, accept user input until that causes the scene to end."""
        while not self.proceed:
            user_input = console.user_action(objects=self.objects)
            valid_object = user_input.noun in self.objects
            valid_command = valid_object and user_input.verb in self.objects[user_input.noun].actions
            if not valid_command:
                self.invalid_command(user_input)
            else:
                action = self.objects[user_input.noun].actions[user_input.verb]
                assert (callable(action)), "Invalid action " + action
                self.proceed = action()

    def invalid_command(self, command):
        """Output to the user that they have failed to enter proper input, and tell them what input is acceptable."""
        if command.noun is None:
            console.output("Valid objects are:")
            for noun in self.objects:
                console.output(noun + " ", new_line=False)
        else:
            console.output(f"Valid actions for the {command.noun} object are:")
            for action in self.objects[command.noun].actions:
                console.output(action + " ", new_line=False)
        console.end_line()


def pause():
    """Pause the scene for a moment."""
    time.sleep(Scene.pause_time)
