
class Enemy:
    def __init__(self, char):
        self.char = char
        self.key = char

class Empty(Enemy):
    def __init__(self):
        super().__init__(" ")
        self.char = "-"

class Goblin(Enemy):
    def __init__(self):
        super().__init__("o")

class Slime(Enemy):
    def __init__(self):
        super().__init__("e")

class KnifeRat(Enemy):
    def __init__(self):
        super().__init__("c")


