from threading import Thread
import time


from functions import create_random_int_list

threads_count = int(input("Threads amount: "))
list_size = int(input("List elements count: "))

if list_size < threads_count:
    # Each thread must at least be resposible for a sublist of 1 element
    raise Exception("List size must be <= threads count")

filled_list = create_random_int_list(list_size)
sums = [0 for _ in range(threads_count)]

def thread_list_sum(id: int, number_list: list[int]):
    sums[id] = sum(number_list)

threads: list[Thread] = []

remainig_threads = threads_count

remainder = list_size % threads_count
matching_threads_count_and_list_size = remainder == 0
iteration_offset = remainder if not matching_threads_count_and_list_size else list_size // threads_count
prev_iteration_offset = 0
current_iteration_offset = iteration_offset

for idx in range(threads_count):
    if remainig_threads == 1:
        thread_list = filled_list[prev_iteration_offset:]
    else:
        thread_list = filled_list[prev_iteration_offset:current_iteration_offset]
    threads.append(Thread(target=thread_list_sum, args=(idx, thread_list)))
    prev_iteration_offset = current_iteration_offset
    current_iteration_offset += iteration_offset
    remainig_threads -= 1


start_time = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(sum(sums))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time} seconds")
