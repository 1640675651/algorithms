/*Longest Common Sequence DP

Input: two strings a and b.

Define dp[i][j]: the length of the longest common sequence of a[0, i] and b[0, j], inclusive.

Formula:

dp[i][j] = dp[i-1][j-1] + 1 			if a[i] == b[j]
			
dp[i][j] = max(dp[i-1][j],dp[i][j-1])	otherwise

// dp is an non-decreasing sequence for i and j. i.e. dp[i+1][j] >= dp[i][j], dp[i][j+1] >= dp[i][j]
// so only need to compare dp[i-1][j] and dp[i][j-1], which are the two possible largest known element in dp.
		
Initial condition:

//dp[0][0] = 1 if a[0] == b[0]
//dp[i][0] = 1 if any a[x from 0 to i] == b[0]
//dp[0][j] = 1 if any a[y from 0 to j] == a[0]
// we can just start i, j from 1 and set the first row and column of dp to 0.
// in this case there is no need to manually initialize dp.

Answer:
dp[n][n]

Code:*/

int dp[1001][1001];
char s1[1001];
char s2[1001];

int LCS(int n, char* s1, char* s2)
{

	int i,j,ans=0;
	memset(dp,0,sizeof(dp));
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(s1[i]==s2[j])
			{
				dp[i][j] = dp[i-1][j-1]+1; //dp[i-1][j-1]+1 is large or equal to dp[i-1]][j] and dp[i][j-1] so no need to compare them
				// because dp[i-1][j] is at most dp[i-1][j-1]+1 and the same for dp[i][j-1]
			}
			else
			{
				dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
			}
		}
	}
	/*for(i=0;i<l1;i++)
		for(j=0;j<l2;j++)
			if(dp[i][j]>ans)
				ans=dp[i][j]; again, dp is increasing, so dp[n][n] is guaranteed to be the largest element*/
	return dp[n][n];
}

// memory optimization: rolling array
// idea: notice dp[i][j] only depends on dp[i-1][j], dp[i][j-1] and dp[i-1][j-1], which are the last "row" and "column" in the dp table
// The last "column" is computed in the loop of j. We only need to keep the last row.
int dp[2][1001];

void swap(int& a, int& b)
{
	int tmp = a;
	a = b;
	b = tmp;
}

int LCS(int n, char* s1, char* s2)
{

	int i,j,ans=0;
	memset(dp,0,sizeof(dp));
	int lastrow = 0;
	int thisrow = 1;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(s1[i]==s2[j])
			{
				dp[thisrow][j] = dp[lastrow][j-1]+1;
			}
			else
			{
				dp[thisrow][j]=max(dp[lastrow][j],dp[thisrow][j-1]);
			}
		}
		swap(lastrow, thisrow);
	}

	return dp[lastrow][n];
}