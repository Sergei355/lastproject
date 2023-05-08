import random
import string
from human import Human

class HumanCreator:
    @staticmethod
    def create(size=10):
        humans = []
        NAMES = ("Alex", "Peter", "Garry", "Alice", "Vladimir",
                 "Olga", "Anna", "Kate", "Victor", "Max")

        MAX_AGE = 120
        MIN_AGE = 1

        for _ in range(size):
            human = Human()
            human.name = random.choice(NAMES)
            human.name += " " + random.choice(string.ascii_uppercase) + "."
            human.age = random.randint(MIN_AGE, MAX_AGE)
            human.is_alive = random.choice((True, False))
            humans.append(human)

        return humans