class Human:

    def __init__(self, name='no name', age=1, alive=True):
        self.__name = name
        self.__age = age
        self.__alive = alive

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and 0 < age <= 120:
            self.__age = age

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, alive):
        if isinstance(alive, bool):
            self.__alive = alive

    def __str__(self):
        return f"{self.__name}: age = {self.__age}. " \
               f"Is alive? - {'YES' if self.__alive else 'NO'}"



