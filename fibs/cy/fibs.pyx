import sys

cdef long long fibs(int n):
    if (n <= 1):
        return 1
    else:
        return fibs(n - 1) + fibs(n - 2)

print fibs(int(sys.argv[1]))
