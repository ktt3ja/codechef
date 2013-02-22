# The only two factors of 10 are 2 and 5. To determine the number of 0's
# at the end of n! for some n, first we notice that since there are more
# factors of 2's than 5's in the prime factorization of the factorial, the
# number 0's at the end of n! is determined by how many factors of 5's there 
# are. That is, the number of 0's at the end of n! equals e
# where e is the highest integer such that 5^e divides n!

# The approach this algorithm takes is as follows:
# First, let S_1 = {x | 0 < x <= n, x divisible by 5}. This determines
# all the factors of n! that contribute at least one factor of 5.
# Note that s_1 = |S_1| = floor(n / 5)
# Let S_2 = {x | 0 < x <= n, x divisible by 5^2}. This determines all
# the factors of n! that contribute at least two factors of 5.
# Note that s_2 = |S_2| = floor(s_1 / 5)
# Repeat until S_k = {x | 0 < x <= n, x divisible by 5^k} so that
# s_k = |S_k| = floor(s_{k-1} / 5) < 5
# Then answer is s_1 + s_2 + ... + s_k


def Z(n):
    result = 0
    while n >= 5:
        n /= 5
        result += n
    return result

if __name__ == "__main__":
    num_times = int(raw_input())
    for i in xrange(num_times):
        n = int(raw_input())
        print Z(n)
