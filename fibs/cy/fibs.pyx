import sys

def fibs(long long n):
    if (n <= 1):
        return 1
    else:
        return fibs(n - 1) + fibs(n - 2)

def main():
    print fibs(int(sys.argv[1]))

if __name__ == "__main__":
    main()
