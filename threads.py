import time


from functions import create_random_int_list, get_threads_for_list

threads_count = int(input("Threads amount: "))
list_size = int(input("List size: "))


numbers_list = create_random_int_list(list_size)
threads_sums = [0 for _ in range(threads_count)]

threads = get_threads_for_list(threads_count, numbers_list, threads_sums)


start_time = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Total sum: {sum(threads_sums)}")
end_time = time.time()
print(f"Elapsed time: {end_time - start_time} seconds")
