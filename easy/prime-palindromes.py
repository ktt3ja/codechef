import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    k = 1
    while (6*k - 1) <= math.sqrt(n):
        if n % 2 == 0 or n % 3 == 0 or \
           n % (6*k - 1) == 0 or n % (6*k + 1) == 0:
            return False
        k += 1
    return True

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Positive integer argument only
def all_nines(n):
    while n >= 1:
        if n % 10 != 9:
            return False
        n /= 10
    return True 

# Assume that n is already a palindrome
def next_palindrome(n):
    if all_nines(n):
        return n + 2
    s = str(n)
    mid = len(s) // 2
    if len(s) % 2 == 0:
        first_half = str(int(s[:mid]) + 1)
        second_half = first_half[::-1]
    else:
        first_half = str(int(s[:mid+1]) + 1)
        second_half = first_half[:mid][::-1]
    return int(first_half + second_half)


if __name__ == '__main__':
    n = int(raw_input())
    while not is_palindrome(str(n)):
        n += 1
    while True:
        if is_prime(n):
            print n
            break
        else:
            n = next_palindrome(n)
