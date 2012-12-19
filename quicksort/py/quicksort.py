from random import randint
from sys import argv

def quicksort(A):
    if len(A) <= 1:
        return A
    pivot_index = randint(0, len(A) - 1)
    pivot, A[pivot_index] = A[pivot_index], None
    less, greater = [], []
    for x in A:
        if x is None:
            continue
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    with open(argv[1]) as f:
        A = map(int, f.read().splitlines())
        quicksort(A)
