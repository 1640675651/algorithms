#include<iostream>
#include<queue>
#include<vector>
using namespace std;

int n,m,s;
const int inf = 2000000000;

vector<pair<int, int> > al[100001];
int d[100001];
bool vis[100001];

struct node
{
	int no;
	int dist;
}tmp;

struct cmp
{
	bool operator()(node a, node b)
	{
		return a.dist > b.dist;
	}
}

priority_queue<node, vector<node>, cmp> q;

void dijk(int o)
{
	vis[o] = 1;
	for(int i=1;i<=n;i++)
	{
		d[i] = inf;
	}
	d[o] = 0;
	int k;

	for(int i=0;i<al[o].size();i++)
	{
		int t = al[o][i].first;
		int w = al[o][i].second;
		d[t] = w;
		tmp.no = t;
		tmp.dist = w;
		q.push(tmp);
	}

	for(int i=1;i<=n-1;i++)
	{
		if(q.empty()) break;
		while(!q.empty())
		{
			tmp = q.top();
			if(vis[tmp.no] == true)
			{
				q.pop();
				continue;
			}
			k = tmp.no;
			break;
		}

		vis[k] = 1;
		// update d
		for(int j=0;j<al[k].size();j++)
		{
			int t = al[k][j].first;
			int w = al[k][j].second;
			if(d[k] + w < d[t] && vis[t] == 0)
			{
				d[t] = d[k] + w;
				tmp.no = t;
				tmp.dist = d[t];
				q.push(tmp);
			}
		}
	}
}

int main()
{
	cin>>n>>m>>s;
	int a, b, w;
	for(int i=0;i<m;i++)
	{
		cin>>a>>b>>w;
		al[a].push_back(make_pair(b, w));
		al[b].push_back(make_pair(a, w));
	}
}