import time
from collections import Counter


def n_counter(l):
    start_time = time.time()
    n_counted = {i: l.count(i) for i in l}
    end_time  = time.time() - start_time
    print("N Counter Time", end_time)

def c_counter(l):
    start_time = time.time()
    c_counted = Counter(l)
    end_time = time.time() - start_time
    print("C Counter Time", end_time)

my_list = list(range(100000))

print("STARTED COUNTER, collections.Counter")
c_counter(my_list)

print("STARTEDm COUNTER, dict comprehension")
n_counter(my_list)


