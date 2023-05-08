from manager import Manager
from human_creator import HumanCreator

ls = HumanCreator.create(15)

for human in ls:
    print(human)

adult = Manager.count_adult(ls)
underage = Manager.count_underage(ls)

print(f"Adult - {adult}")
print(f"Underage - {underage}")