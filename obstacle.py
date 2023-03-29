from turtle import Turtle

POSITIONS_1 = [(-250, 0), (250, 0)]
POSITIONS_2 = [(0, 250), (0, -250)]
POSITIONS_3 = [(0, 0), (0, 0)]



class Obstacle:
    def __init__(self):
        self.all_obstacles = []

    def create_obstacle_1(self):
        for position in POSITIONS_1:
            new_obstacle = Turtle(shape="square")
            new_obstacle.penup()
            new_obstacle.shapesize(10, 1)
            new_obstacle.color("blue")
            new_obstacle.speed("fastest")
            new_obstacle.goto(position)
            self.all_obstacles.append(new_obstacle)

    def create_obstacle_2(self):
        for position in POSITIONS_2:
            new_obstacle = Turtle(shape="square")
            new_obstacle.penup()
            new_obstacle.shapesize(1, 10)
            new_obstacle.color("blue")
            new_obstacle.speed("fastest")
            new_obstacle.goto(position)
            self.all_obstacles.append(new_obstacle)

    def create_obstacle_3(self):
        for position in POSITIONS_3:
            new_obstacle = Turtle(shape="square")
            new_obstacle.penup()
            new_obstacle.shapesize(1, 15)
            new_obstacle.color("blue")
            new_obstacle.speed("fastest")
            new_obstacle.goto(position)
            self.all_obstacles.append(new_obstacle)
