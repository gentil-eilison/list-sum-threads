import time, random
from threading import Thread

threads_count = int(input("Threads amount: "))
list_size = int(input("List size: "))

if threads_count > list_size:
    raise Exception("Threads count can't be greater than list size")

numbers_list = [random.randint(1, 1_000_000) for _ in range(list_size)]
threads_sums = [0 for _ in range(threads_count)]


def get_iteration_offset(list_size: int, threads_count: int):
    """
    Calculates which value should be the offset for slicing the list
    when splitting it across different threads. E.g.: every 5 elements, every 2 elements, etc.
    """
    remainder = list_size % threads_count
    iteration_offset = remainder if remainder == 1 else list_size // threads_count
    return iteration_offset


def thread_list_sum(id: int, start_idx: int, end_idx: int|None = None):
    thread_list = []
    if end_idx:
        thread_list = numbers_list[start_idx:end_idx]
    else:
        thread_list = numbers_list[start_idx:]
    thread_total_sum = 0
    for number in thread_list:
        thread_total_sum += number
    threads_sums[id] = thread_total_sum


def get_threads_for_list(threads_count: int):
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
            threads.append(
                Thread(target=thread_list_sum, args=(idx, current_slice_start))
            )
        else:
            threads.append(
                Thread(target=thread_list_sum, args=(idx, current_slice_start, current_slice_end))
            )
        current_slice_start = current_slice_end
        current_slice_end += iteration_offset
        remainig_threads -= 1
    return threads


threads = get_threads_for_list(threads_count)

start_time = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

total_sum = 0
for number in threads_sums:
    total_sum += number
end_time = time.time()
print(f"Elapsed time (threads): {end_time - start_time} seconds")

# Trivial
start_time = time.time()
total_sum = 0
for number in numbers_list:
    total_sum += number
end_time = time.time()

print(f"Elapsed time (loop): {end_time - start_time} seconds")
