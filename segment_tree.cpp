#include<cstdio>
#include<iostream>
using namespace std;
int n; // n numbers in array
long long a[100001];
long long sum[400004];
long long ltag[400004]; // tag for lazy update
void pushup(int x)
{
	sum[x]=sum[x*2]+sum[x*2+1];
}
void build(int x,int l,int r)
{
	if(l==r)
	{
		sum[x]=a[l];
		return;
	}
	int m=(l+r)/2;
	build(x*2,l,m);
	build(x*2+1,m+1,r);
	pushup(x);
}
void pushdown(int x,int l,int r)
{
	if(ltag[x])
	{
		int m=(l+r)/2,lchild=x*2,rchild=x*2+1;
		ltag[lchild]+=ltag[x];
		sum[lchild]+=ltag[x]*(m-l+1);
		ltag[rchild]+=ltag[x];
		//sum[x]+=ltag[x]*(r-l+1); no need to update the sum here. pushup will do the job later.
		sum[rchild]+=ltag[x]*(r-m);
		ltag[x]=0;
	}
}
void update(int x,int l,int r,int L,int R,int add) // add a number "add" to each element in an interval [L,R]
// x: node in the tree, l: left bound of node x, r: right bound of node x
{
	if(l>R || r<L)return; // case 1: the current node has no intersection with [L, R]
	if(l>=L && r<=R) // case 2: the current node is totally inside of the interval [L, R]
	{
		// only need to tag the current node, no need to update its children now. This is why the tag is called lazy tag.
		ltag[x]+=add; 
		sum[x]+=add * (r-l+1);
		return;
	}
	// case 3: the current node partially intersects with [L, R]
	int m=(l+r)/2;
	pushdown(x,l,r); // if there is a tag on the current node, need to push the tag to its children and clear its own tag.
	update(x*2,l,m,L,R,add);
	update(x*2+1,m+1,r,L,R,add);
	pushup(x);
}
long long query(int x,int l,int r,int L,int R) // query the sum of the interval [L, R]
{
	if(l>R || r<L)return 0;
	if(l>=L && r<=R)return sum[x];
	int m=(l+r)/2;
	pushdown(x,l,r);
	return query(x*2,l,m,L,R)+query(x*2+1,m+1,r,L,R); 
}

// build(1, 1, n);				to build tree
// update(1, 1, n, L, R, add)	to add a number to [L, R]
// query(1, 1, n, L, R)			to query the sum of [L, R]
