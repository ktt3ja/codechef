# Statement
# 
# You need to find a string which has exactly K positions in it such that the
# character at that position comes alphabetically later than the character
# immediately after it. If there are many such strings, print the one which
# has the shortest length. If there is still a tie, print the string which
# comes the lexicographically earliest (would occur earlier in a dictionary).
#
# Input
# The first line contains the number of test cases T. Each test case contains
# n integer K (<= 100).
#
# Output
# Output T lines, one for each test case, containing the required string. Use
# only lower-case letters a-z.
#
# Sample Input
# 2
# 1
# 2
#
# Sample Output
# ba
# cba

import math

def produce_dstring(n):
    if n == 0:
        return ''
    s = 'abcdefghijklmnopqrstuvwxyz'
    i = (n % 25) if n % 25 != 0 else 25
    times = int(math.ceil(float(n)/25) - 1)
    dstring = [s[:i+1][::-1]]
    for _ in xrange(0, times):
        dstring.append(s[::-1])
    return ''.join(dstring)

if __name__ == '__main__':
    times = int(raw_input())
    for _ in xrange(0, times):
        n = int(raw_input())
        print(produce_dstring(n))
