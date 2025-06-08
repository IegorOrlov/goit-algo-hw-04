from collections import defaultdict
import random


def getSamples(
    start_size: int = 1,
    end_size: int = 10**4,
    arraise_per_size: int = 10,
    random_range: int = 10**4
) -> dict[int, list[list[int]]]:
    samples = defaultdict(list)
    for size in range(start_size, end_size):
        for n in range(arraise_per_size):
            samples[size].append([random.randint(1, random_range) for _ in range(size)])
    return samples

