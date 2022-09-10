#https://www.codewars.com/kata/53f1015fa9fe02cbda00111a

import random

class Ghost():
  def colour(self):
    self.colour = random.choice(["white", "yellow", "purple", "red"])
    return self.colour

ghost = Ghost()
print(ghost.colour())
