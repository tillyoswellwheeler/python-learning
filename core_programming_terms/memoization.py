# --------------------------------
# Programming Terms -- Memoization
# --------------------------------
import time

ef_cache = {}

def expensive_function(num):
    if num in ef_cache:
        return ef_cache[num]

    print("Computing {}...".format(num))
    time.sleep(1)
    result = num * num
    ef_cache[num] = result
    return result


start_time = time.time()

result = expensive_function(6)
print(result)

result = expensive_function(10)
print(result)

result = expensive_function(6)
print(result)

result = expensive_function(10)
print(result)

end_time = time.time()

print(end_time - start_time, 's')