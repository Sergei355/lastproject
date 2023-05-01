class human:
    def __init__(self, first_name='no name', surname='no name', age=16, alive=True):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.alive = alive

    def str(self):
        msg = self.first_name
        msg += " is alive " if self.alive else " is dead"
        msg += " with age = " + str(self.age)
        return msg








