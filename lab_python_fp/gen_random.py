import random


def gen_random(size: int, min, max):
    for _ in range(size):
        yield random.randint(min, max)