import random

from threading import Thread


def create_random_int_list(size: int) -> list[int]:
    return [random.randint(1, 1_000_000) for _ in range(size)]


