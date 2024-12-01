from math import sqrt
from typing import Union
from enemy import *

class Level:
    def __init__(self, level_gen):
        self.level_gen = level_gen
        self.steps = 0
        self.length = 40


    def get_next_step(self) -> Union[Enemy, None]:
        self.steps += 1
        return self.level_gen(self.steps)


class LevelLibrary:
    def __init__(self, levels):
        self.levels = levels
        self.current_level = 0

    def __iter__(self):
        return self

    def __next__(self):
        next_level = self.get_level(self.current_level)

        if next_level is None:
            raise StopIteration

        self.current_level += 1
        return next_level

    def get_level(self, level_number: int) -> Union[Level, None]:
        if level_number >= len(self.levels):
            return None
        else:
            return Level(self.levels[level_number])


level_lib = LevelLibrary(
[
    lambda step : Goblin() if step%2==0 else Empty(),
    lambda step : Goblin() if step%3==0 else Empty(),
    lambda step : Goblin() if step%4==0 else KnifeRat() if step%2==0 else Empty(),
    lambda step : Slime() if sqrt((step * 8) + 1).is_integer() else Empty(),
    lambda step : KnifeRat() if step%3==0 and step%5==0 else Goblin() if step%3==0 else Slime() if step%5==0 else Empty(),
]
)