from data import getSamples
from sort_algs import insertion_sort, merge_sort
import timeit
import statistics as st
from typing import Callable
import matplotlib.pyplot as plt


def get_mean_time(lsts: list[list[int]], sort: Callable[[list[int]], list]) -> float:
    return st.mean([timeit.timeit(lambda: sort(lst.copy()), number=10) for lst in lsts])


def create_histogram(samples: dict[int, list[list[int]]], sort: Callable[[list[int]], list], color: str):
    x = list(samples.keys())
    y = [get_mean_time(lsts, sort) for lsts in samples.values()]

    plt.bar(x, y, width=1, color=color, edgecolor="black", alpha=0.5)
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час")


samples = getSamples(end_size=200)

create_histogram(samples, insertion_sort, "blue")
create_histogram(samples, merge_sort,"green")
create_histogram(samples, sorted, "red")
plt.show()
