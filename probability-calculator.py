import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        for k, v in self.balls.items():
            for i in range(v):
                self.contents.append(k)
        print(self.contents)
        self.original_contents = self.contents.copy()

    def draw(self, balls_to_draw):
        balls_to_draw = balls_to_draw
        balls_drawn = []
        if balls_to_draw > len(self.contents):
            self.contents = self.original_contents.copy()
        for i in range(balls_to_draw):
            random_index = random.randint(0, len(self.contents)-1)
            balls_drawn.append(self.contents[random_index])
            self.contents.pop(random_index)

        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiments_run = 0
    experiments_success = 0
    expected_balls_dict = expected_balls
    expected_balls = []
    for k, v in expected_balls_dict.items():
        for i in range(v):
            expected_balls.append(k)

    while num_experiments != 0:
        balls_drawn = hat.draw(num_balls_drawn)
        if all(x in expected_balls for x in balls_drawn):
            experiments_success += 1
            # print('experiment successful')
            # print(balls_drawn)
            # print(expected_balls)
        experiments_run += 1
        num_experiments -= 1
    # print(experiments_success)
    # print(experiments_run)
    return (experiments_success / experiments_run)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)