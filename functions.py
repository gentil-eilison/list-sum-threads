import random

from threading import Thread


def create_random_int_list(size: int) -> list[int]:
    return [random.randint(1, 1_000_000) for _ in range(size)]


def get_iteration_offset(list_size: int, threads_count: int):
    """
    Calculates which value should be the offset for slicing the list
    when splitting it across different threads. E.g.: every 5 elements, every 2 elements, etc.
    """
    remainder = list_size % threads_count
    if list_size - threads_count == 2:
        return 1
    iteration_offset = remainder if remainder != 0 else list_size // threads_count
    return iteration_offset


def thread_list_sum(id: int, number_list: list[int], sums_list: list[int]):
    sums_list[id] = sum(number_list)


def get_threads_for_list(threads_count: int, numbers_list: list[int], sums_list: list[int]):
    """
    Logic for sharing sum work across threads:
    If the number of elements / number of threads has 0 as a remainder, then use the
    quocient as the offset. Use the remainder otherwise. When there is only one thread
    remainig, pass what's left of the list to the remaining thread. 
    """
    threads = []
    iteration_offset = get_iteration_offset(len(numbers_list), threads_count)
    current_slice_end = iteration_offset
    current_slice_start = 0
    remainig_threads = threads_count

    for idx in range(threads_count):
        if remainig_threads == 1:
            thread_list = numbers_list[current_slice_start:]
        else:
            thread_list = numbers_list[current_slice_start:current_slice_end]
        threads.append(
            Thread(target=thread_list_sum, args=(idx, thread_list, sums_list))
        )
        current_slice_start = current_slice_end
        current_slice_end += iteration_offset
        remainig_threads -= 1
    return threads
