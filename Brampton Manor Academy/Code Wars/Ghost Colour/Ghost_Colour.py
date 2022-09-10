import random

class Ghost():
  def colour(self):
    self.colour = random.choice(["white", "yellow", "purple", "red"])
    return self.colour

ghost = Ghost()
print(ghost.colour())
