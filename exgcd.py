# Goal: Find x, y that satisfies a*x + b*y = gcd(a,b)
# i.e. express gcd(a,b) as a linear combination of a and b

# idea: in each step of the Euclidean algorithm, a % b is computed.
# a % b is already expressed as a linear combination of a and b.
# a = b*(a//b) + a % b
# a % b = a - b*(a//b)
# Now a % b is expressed as a linear combination of a and b: 1 * a - (a//b) * b.
# The two coefficients are 1 and -a//b, which are shown in l2 in the prep function below.

# Step 1: Preperation
# Let the list of numbers generated in the gcd process be l1.
# Let the coefficients of linear combination be l2.
# That is, l1[i] = l2[i][0] * l1[i-2] + l2[i][1] * l1[i-1] (Eq.1),
# Where l2[i][1] = -l1[i-2] // l1[i-1]
# Notice the first coefficient is always 1, we can just let l2 be and 1D array, only storing the second coefficient.

# Step 2: Recursion Relation
# Now our goal is to express l1[-1] as a linear combination of l1[0] and l1[1].
# Suppose we have a magical function exgcd(i) that returns the linear combination of l1[i] in l1[0] and l1[1], the coefficients form a tuple of 2 elements.
# Expressing l1[i-1] and l1[i-2] in exgcd:
# l1[i-1] = exgcd(i-1)[0] * l[0] + exgcd(i-1)[1] * l[1]
# l1[i-2] = exgcd(i-2)[0] * l[0] + exgcd(i-2)[1] * l[1]

# Plug these values into the definition of l2 (Eq.1):
# l1[i] = l2[i][0] * l1[i-2] + l2[i][1] * l1[i-1]
#       = l2[i][0] * (exgcd(i-2)[0] * l1[0] + exgcd(i-2)[1] * l1[1]) + l2[i][1] * (exgcd(i-1)[0] * l1[0] + exgcd(i-1)[1] * l1[1])
#       = (l2[i][0] * exgcd(i-2)[0] + l2[i][1] * exgcd(i-1)[0]) * l1[0] + (l2[i][0] * exgcd(i-2)[1] + l2[i][1] * exgcd(i-1)[1]) * l1[1]  (Just pulling out l1[0] and l1[1])
# The coefficient of l1[0] is (l2[i][0] * exgcd(i-2)[0] + l2[i][1] * exgcd(i-1)[0]) (Call it c1)
# The coefficient of l1[1] is (l2[i][0] * exgcd(i-2)[1] + l2[i][1] * exgcd(i-1)[1]) (Call it c2)

# Now we have a recursion relation: exgcd(i) = (c1, c2). Up to now we can actually implement the function recursively.
# Notice the base case: l1[0] and l1[1] are justs linear combination of themselves.


def prep(a,b):
    l1 = [a,b]
    l2 = [None,None]
    while l1[-2] % l1[-1] != 0:
        l1.append(l1[-2] % l1[-1]) # l1: record every number generated in the gcd progress. l1[-1] is gcd(a,b)
        l2.append((1,-(l1[-3]//l1[-2]))) # l2: record how the current number can be represented by a linear combination of the last two numbers
    return l1,l2

def exgcd(n, l1, l2): #brute recursive algorithm
    if n == 0:
        return (1,0)
    if n == 1:
        return (0,1)

    return (exgcd(n-2, l1, l2)[0] * l2[n][0] + exgcd(n-1, l1, l2)[0] * l2[n][1] , exgcd(n-2, l1, l2)[1] * l2[n][0] + exgcd(n-1, l1, l2)[1] * l2[n][1])

# The performance of recursive implementaion sucks.
# There should be a smarter linear algorithm.
# Do it in an iterative way (just like memoizing the result of each exgcd call):
# Using the same relationship, just replacing exgcd(i-1), exgcd(i-2) to dp[i-1], dp[i-2]

def exgcd_dp(l2): #dp time complexity optimization O(2^n) -> O(n)
    dp = [(1,0), (0,1)] #dp[i]: records how the ith number can be represented by a linear combination of a and b(the numbers inputed)
    for i in range(2, len(l2)):
        dp.append((dp[i-2][0] * l2[i][0] + dp[i-1][0] * l2[i][1], dp[i-2][1] * l2[i][0] + dp[i-1][1] * l2[i][1]))
    return dp[-1]

# Notice, each iterative step only depends on the last 2 elements of the dp array.
# Only need to keep track of 2 elements.
def exgcd_dp1(l2): #space complexity optimization O(n) -> O(1)
    last2, last1 = (1,0), (0,1)
    current = last1 # for the case b evenly divides a
    for i in range(2, len(l2)):
        current = (last2[0] * l2[i][0] + last1[0] * l2[i][1], last2[1] * l2[i][0] + last1[1] * l2[i][1])
        last2, last1 = last1, current
    return current

# it works for a>b or a<b, a|b or b|a.
if __name__ == '__main__':
    a,b = input().split()
    a = eval(a)
    b = eval(b)
    l1, l2 = prep(a,b)
    #print(exgcd(len(l1) - 1, l1, l2))
    #print(exgcd_dp(l2))
    print(exgcd_dp1(l2))

# Usage for finding Modular Multiplicative Inverse:
# Definition of Modular Multiplicative Inverse:
# x is the MMI of a (mod b) if ax % b = 1
# In other words, xa + yb  = 1

# We know gcd(a,b) = xa + yb
# When gcd(a,b) = 1, exgcd gives us exactly x and y.
# x is the answer.
# x can be negative sometimes, mod b to make it positive.
