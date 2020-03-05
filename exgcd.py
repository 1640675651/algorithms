def prep(a,b):
    l1 = [a,b]
    l2 = [None,None]
    while l1[-2] % l1[-1] != 0:
        l1.append(l1[-2] % l1[-1]) # l1: record every number generated in the gcd progress
        l2.append((1,-(l1[-3]//l1[-2]))) # l2: record how the current number can be represented by a linear combination of the last two numbers
    return l1,l2

def exgcd(n, l1, l2): #brute recursive algorithm
    if n == 0:
        return (1,0)
    if n == 1:
        return (0,1)

    return (exgcd(n-2, l1, l2)[0] * l2[n][0] + exgcd(n-1, l1, l2)[0] * l2[n][1] , exgcd(n-2, l1, l2)[1] * l2[n][0] + exgcd(n-1, l1, l2)[1] * l2[n][1])

def exgcd_dp(l2): #dp time complexity optimization O(2^n) -> O(n)
    dp = [(1,0), (0,1)] #dp[i]: records how the ith number can be represented by a linear combination of a and b(the numbers inputed)
    for i in range(2, len(l2)):
        dp.append((dp[i-2][0] * l2[i][0] + dp[i-1][0] * l2[i][1], dp[i-2][1] * l2[i][0] + dp[i-1][1] * l2[i][1]))
    return dp[-1]

def exgcd_dp1(l2): #space complexity optimization O(n) -> O(1)
    last2, last1 = (1,0), (0,1)
    current = ()
    for i in range(2, len(l2)):
        current = (last2[0] * l2[i][0] + last1[0] * l2[i][1], last2[1] * l2[i][0] + last1[1] * l2[i][1])
        last2, last1 = last1, current
    return current

if __name__ == '__main__':
    a,b = input().split()
    a = eval(a)
    b = eval(b)
    l1, l2 = prep(a,b)
    #print(exgcd(len(l1) - 1, l1, l2))
    #print(exgcd_dp(l2))
    print(exgcd_dp1(l2))
