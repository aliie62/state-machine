from random import choice

def randomiser(*args,start,end)->int:
    """
    Generates a random integer number
        Start and End are inclusive
        *args accept any number of excluded edges (transitions) from
            the randomision result
    """
    *exclusion, = args
    return choice([i for i in range(start,end+1) if i not in exclusion])