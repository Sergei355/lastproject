from Human import human

def find_humans(humans):

    target = humans[0]

    for human in humans:
            if human.age > 18:
                target = human

    return target