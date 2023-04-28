class human:
    def __init__(self, first_name='no name', surname='no name', age=16, alive=True):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.alive = alive

    def __str__(human1):
        msg = self.first_name
        msg += "Is still alive" if self.alive else "Is dead"
        msg += self.age + "Age: "
        return msg



    # def __str__(self):
    #     msg = self.__first_name
    #     msg += ("Is still alive"
    #             if self.__alive else "Is dead")
