from Human import human
from managment import find_humans

def main():
    human1 = human("Alex", "Mad", 42, True)
    human2 = human("Petr", "Ivanov", 22, True)
    human3 = human("Masha", "Suhotskaya", 45, True)
    human4 = human("Victoria", "Sadovskaya", 18, True)
    human5 = human("Sergei", "Slizevich", 33, True)

    humans = (human1, human2, human3, human4, human5)

    result = find_humans(humans)
    print(result)

if __name__ == '__main__':
    main()
