import time
from functions import create_random_int_list


list_size = int(input("List elements count: "))

filled_list = create_random_int_list(list_size)

start_time = time.time()
print(sum(filled_list))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time}")

