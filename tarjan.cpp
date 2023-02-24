/*Tarjan: compute strongly connected components (SCC)
maintain variable dfu and low for each vertex.
dfn[u]: The order node n being visited in the dfs process
low[u]: The lowest node dfn reachable from u. All vertices in a SCC have the same low value.

maintain a stack

Suppose we are currently at u. Do dfs for all v's such that there's and edge u->v. When backtrack (after dfs(v)), update low[u] to min(low[u], low[v]) if v is on stack.

When find an SCC (dfn[u] == low[u]) after all dfs from u finishes, remove all elements from the stack. */

#include<iostream>
#include<vector>
using namespace std;

int n, m;
vector<int> al[100];
bool vis[100];

int dfn[100];
int maxdfn;
int low[100];

bool onstack[100];
int stack[100];
int stacklen;
int scccnt;

void dfs(int v)
{
	// record the order v being searched
	dfn[v] = maxdfn;
	// set low to itself
	low[v] = dfn[v];
	maxdfn++;

	// push v into the stack
	stack[stacklen] = v;
	stacklen++;
	onstack[v] = true;
	vis[v] = true;

	// do dfs
	for(int i=0;i<al[v].size();i++)
	{
		int next = al[v][i];
		if(!vis[next])
		{
			dfs(next);
		}
		if(onstack[next])
		{
			low[v] = min(low[v], low[next]);
		}
	}

	// check whether a SCC was found
	if(low[v] == dfn[v]) // SCC found
	{
		// pop all the nodes in the current SCC from the stack
		while(stacklen > 0)
		{
			// pop 1 node from the stack until the start of the SCC (inclusive)
			stacklen--;
			onstack[stack[stacklen]] = false;
			//low[stack[stacklen]] = dfn[v]; // It seems this is not needed since the min(low) operation is done in the dfs
			if(stack[stacklen] == v) //notice here is v, not dfn[v] since the stack stores vertex number
				break;
		}
		
		scccnt++;
	}

}

int main()
{
	cin>>n>>m;
	for(int i=0;i<m;i++)
	{
		int f, t;
		cin>>f>>t;
		al[f].push_back(t);
	}
	for(int i=0;i<n;i++)
	{
		if(!vis[i])
			dfs(i);
	}
	cout<<scccnt<<endl;
	for(int i=0;i<n;i++)
	{
		cout<<low[i]<<" ";
	}
	cout<<endl;
}