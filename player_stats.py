
class PlayerStats:
    def __init__(self):
        self.lives = 10

    def lose_life(self):
        self.lives -= 1

    def heal_life(self):
        if self.lives < 10:
            self.lives += 1

    def is_dead(self):
        if self.lives <= 0:
            return True
        else:
            return False