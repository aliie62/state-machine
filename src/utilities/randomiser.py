from random import choice

def randomiser()->int:
    """
    Generates a random integer
    """

    return choice([i for i in range(1,27)])
