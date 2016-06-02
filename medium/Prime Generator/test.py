import sys, re, math

cache = {0:False}

def isPrime(n):
    #  make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2 : return False
    # 2 is the only even prime number
    if n == 2 : return True
    # all other even numbers are not primes
    if not n & 1 : return False
    # range starts with 3 and only need to go up to the squareroot of n
    # for all odd numbers
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

def print_prime (num1, num2):
    for x in range(num1, num2+1):
        if (isPrime(x)):
            print x

if __name__ == "__main__":
    try:
        num = int(raw_input())
        for i in range(0,num):
            line = raw_input()

            m = re.match("([0-9]+) ([0-9]+)",line)

            num1 = int(m.group(1))
            num2 = int(m.group(2))

            print_prime(num1,num2)
            if i < num-1 :
                print

    except Exception, e:
            print str(e)