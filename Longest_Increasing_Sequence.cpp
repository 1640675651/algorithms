int dp[100001];
int h[100001];
const int inf = 2147483647;

int bs(int x, int l, int r) // binary search, find the rightmost element that is strictly less than x
{							// suppose the array is non-decreasing
	while(l < r-1)
	{
		int mid = (l+r)/2;
		if(dp[mid] < x)
		{				 
			l = mid;
		}
		else
		{
			r = mid;
		}
	}
	if(dp[r] < x)
		return r;
	return l;
}

int LIS() // longest (strictly) increasing sequence
{
	dp[0] = -inf;
	int dplen = 0;
	for(int i=1;i<=n;i++)
	{
		if(h[i] > dp[dplen])
			dp[++dplen] = h[i];
		else
		{
			int x = bs(h[i], 0, dplen); // dp[x] is the rightmost element that is strictly less than x, so h[i] can be put after dp[x]
			dp[x+1] = h[i];
		}
	}
	return dplen;
}