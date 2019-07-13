# -*- coding: UTF-8
from ..console import Console


class Scene:
    def __init__(self, setup):
        self.setup = setup

    def play(self):
        for line in self.setup:
            if type(line) is str:
                Console.output(line, False)
            if callable(line):
                line()
        Console.end_line()

    def action(self):
        pass
