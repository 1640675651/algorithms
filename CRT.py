# Chinese Remainder Theorem (CRT)
# Goal: Given a set of Linear Congruence Equations (all n's are relatively prime):
# x % n1 = a1 % n1
# x % n2 = a2 % n2
# ...
# x % nk = ak % nk
# find x

def prep(a,b):
    l1 = [a,b]
    l2 = [None,None]
    while l1[-2] % l1[-1] != 0:
        l1.append(l1[-2] % l1[-1]) # l1: record every number generated in the gcd progress. l1[-1] is gcd(a,b)
        l2.append((1,-(l1[-3]//l1[-2]))) # l2: record how the current number can be represented by a linear combination of the last two numbers
    return l1,l2

def exgcd_dp1(l2): #space complexity optimization O(n) -> O(1)
    last2, last1 = (1,0), (0,1)
    current = last1 # for the case b evenly divides a
    for i in range(2, len(l2)):
        current = (last2[0] * l2[i][0] + last1[0] * l2[i][1], last2[1] * l2[i][0] + last1[1] * l2[i][1])
        last2, last1 = last1, current
    return current

def mi(a, b):
    '''multiplicative inverse of a (mod b), not to be confused with m_i below'''
    l1, l2 = prep(a,b)
    mul_inv = exgcd_dp1(l2)[0] # the first element is the answer
    return mul_inv % b # make it positive
    
def crt(a: list, n: list):
    # Step 1: calculate the product of all modular numbers in list n
    nprod = 1
    for i in n:
        nprod *= i

    # Step 2: for the ith equation,
    ans = 0
    for i in range(len(n)):
        # Step 2.1 calculate m_i = nprod//n_i
        m_i = nprod//n[i]

        # Step 2.2 calculate the Multiplicative Inverse of mi (mod ni), m_i_inv
        m_i_inv = mi(m_i, n[i])

        # Step 2.3 calculate c_i = m_i * m_i_inv
        c_i = m_i * m_i_inv
        ans += a[i] * c_i;

    # Step 3: the answer is sum(a_i*c_i) % nprod.
    return ans % nprod

if __name__ == '__main__':
    k = int(input())
    a = [0] * k # a is the remainder
    n = [0] * k # n is the modular number
    for i in range(k):
        x, y = input().split()
        a[i] = int(x)
        n[i] = int(y)

    print(crt(a, n))
        
# Extended CRT
# Addresses the case that the modular numbers are not relatively prime.
# First consider the case of two equations:
# x % n1 = a1 % n1, x % n2 = a2 % n2.
# Convert them to undetermined equation:
# x = n1*p+a1 = n2*q+a2, where p and q are integers
# n1*p - n2*q = a2 - a1
# Using Bezout's identity, when a2-a1 cannot be evenly divided by gcd(n1, n2), there is no solultion.
# Otherwise can express (a2 - a1) as a linear combination of gcd(n1, n2) using exgcd,
# then express (a2 - a1) as a linear combination of n1 and n2, producing one solution for (p, q), and we can get x.

# For multiple (more than 2) equations,
# Write the solution above in the form of linear congruent equation:
# x % M = b % M, where b = n1*p + a1 (n2*q + a2 is also fine), M = lcm(m1, m2).
# In this case we eliminated 2 equations, and added 1 new equation to the equation set.
# Do this elimination until there's only 1 equation.
