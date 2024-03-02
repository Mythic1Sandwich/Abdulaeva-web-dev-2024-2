# process_list.py

import time
def process_list(arr):
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)

    return result



def process_list_comprehension(arr):
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def process_list_gen(arr):
    for i in arr:
        if i % 2 == 0:
            yield i ** 2
        else:
            yield i ** 3
        print(i)

if __name__ == '__main__':
    arr = [i for i in range(1, 101)]

    start_time = time.time()
    result = process_list(arr)
    end_time = time.time()
    print(f"process_list execution time: {end_time - start_time} seconds")

    start_time = time.time()
    result_comprehension = process_list_comprehension(arr)
    end_time = time.time()
    print(f"process_list_comprehension execution time: {end_time - start_time} seconds")

    start_time = time.time()
    result_gen = list(process_list_gen(arr))
    end_time = time.time()
    print(f"process_list_gen execution time: {end_time - start_time} seconds")

    # ВЫВОД:
    # process_list_comprehension работает быстрее, чем process_list
    # process_list_gen работает медленнее, чем process_list и process_list_comprehension
