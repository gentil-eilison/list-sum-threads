import time
from functions import create_random_int_list


list_size = int(input("List elements count: "))

numbers_list = create_random_int_list(list_size)

start_time = time.time()
print(f"Total sum: {sum(numbers_list)}")
end_time = time.time()
print(f"Elapsed time: {end_time - start_time}")

