import sys
sys.set_int_max_str_digits(2147483647)
sys.setrecursionlimit(2147483647)
def count(i=2):
    print(i)
    count(i**2)
count()
