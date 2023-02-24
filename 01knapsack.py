def knapsack(maxweight:int, weight: list, value: list):
	# define dp[i][j]: the max value can be obtained when trying to grab the first i items within total weight j
	dp = [0]*(maxweight+1) # Formula: dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[]i), initial condition: dp[0][j] = 0 for any j
    for i in weight:
        for j in range(maxweight, 0, -1): # since we use rolling array, need to loop in reverse order since later dp element depends on earlier dp element
            if j >= i:
                dp[j] = max(dp[j], dp[j-i]+value[i])
            #else:
            #    dp[j] = dp[j]
    return dp[maxweight]
