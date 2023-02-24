int bs1(int* a, int x, int l, int r) // binary search, find the rightmost element that is less than or equal to x
{									 // suppose the array is non-decreasing
	while(l < r-1)
	{
		int mid = (l+r)/2;
		if(a[mid] <= x) // if want the leftmost one when there are multiple values equal to x, remove the =
		{				// if the array is non-increasing, change < to >
			l = mid;
		}
		else
		{
			r = mid;
		}
	}
	if(a[r] <= x)		// if the array is non-increasing, change < to >
		return r;		// if want the leftmost one when there are multiple values equal to x, need to first check if(a[l] == x) return l
	return l;
}

int bs2(int* a, int x, int l, int r) // binary search, find the rightmost element that is less than or equal to x. if multiple x exists in the array, return the leftmost one.
{									 // suppose the array is non-decreasing
	while(l < r-1)
	{
		int mid = (l+r)/2;
		if(a[mid] < x)	
		{				// if the array is non-increasing, change < to >
			l = mid;
		}
		else
		{
			r = mid;
		}
	}
	if(a[r] < x)		// if the array is non-increasing, change < to >
		return r;
	if(a[r] == x && a[l] != x)
		return r;
	return l;
}

int bs3(int* a, int x, int l, int r) // binary search, find the rightmost element that is strictly less than x
{									 // suppose the array is non-decreasing
	while(l < r-1)
	{
		int mid = (l+r)/2;
		if(a[mid] < x) 
		{				 
			l = mid;
		}
		else
		{
			r = mid;
		}
	}
	if(a[r] < x)
		return r;
	return l;
}