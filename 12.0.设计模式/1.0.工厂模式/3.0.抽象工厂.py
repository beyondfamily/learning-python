class Frog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self,obstacle, obstacle.action()))

class Bug:
    def __str__(self):
        return 'a bug'
    def action(self):
        return 'eats it'

class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\t------ Frog World ------'
    def make_character(self):
        return Frog(self.player_name)
    def make_obstacle(self):
        return Bug()

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    def play(self):
        self.hero.interact_with(self.obstacle)


# 选择游戏模式
def validate_age(name):
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid, please try \
        again…".format(age))
        return (False, age)
    return (True, age)


def main():
    name='abb'
    game = FrogWorld
    environment = GameEnvironment(game(name))
    environment.play()



if __name__ == '__main__':
    main()
