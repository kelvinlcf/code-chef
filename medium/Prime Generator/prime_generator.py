#!/usr/bin/python
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

def sieve_prime (num1, num2):
    sieve = [True] * (num2+10)
    sieve[0] = False
    sieve[1] = False
    for i in range(2,int(math.sqrt(num2))+1):
        # print "running i : %d" % (i)
        if sieve[i] :
            for j in range(i*i, num2+1, i):
                # print "running j : %d" % (j)
                sieve[j] = False
    return sieve

def print_array (num1,num2,array) :
    # next_line = False
    # for x in range(num1, num2+1) :
    #     if array[x] : 
    #         if next_line :
    #             print
    #         else:
    #             next_line = True
    #         sys.stdout.write("%d" % x)

    # for x in range(num1, num2+1):
    #     if array[x]:
    #         if isPrime(x):
    #             print x
    #         else :
    #             print "System error : %d......................." %(x)

    for x in range(num1, num2+1):
        if array[x]:
            print x

if __name__ == "__main__":
    try:
        num = int(raw_input())
        for i in range(0,num):
            line = raw_input()

            m = re.match("([0-9]+) ([0-9]+)",line)
            # prime_gen(int(m.group(1)), int(m.group(2)))

            num1 = int(m.group(1))
            num2 = int(m.group(2))

            print_array(num1,num2,sieve_prime(num1,num2))
            if i < num-1 :
                print
            # print
            # sys.stdout.write("%d\n" % break_down(num))
    except Exception, e:
            print str(e)