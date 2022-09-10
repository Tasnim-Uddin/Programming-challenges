#https://www.codewars.com/kata/53f0f358b9cb376eca001079

class Ball(object):
    def __init__(self,ball_type = "regular"):
        self.ball_type = ball_type

if __name__ == "__main__":
    ball1 = Ball()
    ball2 = Ball("super")
    print(f"Ball 1 is a {ball1.ball_type} ball")
    print(f"Ball 2 is a {ball2.ball_type} ball")
