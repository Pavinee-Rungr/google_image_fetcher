import random
from string import ascii_uppercase, digits


def random_string(n):
    return ''.join(random.choice(ascii_uppercase + digits) for _ in range(n))
