#include<iostream>
#include<cstring>
using namespace std;
char s1[1000001];
char s2[1000001];
int kmpnext[1000001];
// definition of kmpnext[i]: the maximum length of the common string of the prefix and suffix of s2[0:i] (inclusive)
// if index starts from 1, change the definition to the maximum length of ... s2[1:i] (inclusive)

// if index starts from 1, just offset every index by 1 and change every 0 into 1 (marked offset).
void getkmpnext(int l2)
{
	// in preprocessing, i starts from 1 and j from 0, since there's no point matching the whole string with itself.
	int i=1, j=0; // offset
	kmpnext[0] = 0;
	while(i<l2)
	{
		if(s2[i] == s2[j])
		{
			kmpnext[i] = j+1;
			i++;
			j++;
		}
		else if(j>0) // offset
		{
			j = kmpnext[j-1];
		}
		else //j = 0 and s2[i]!=s2[j]
		{
			kmpnext[i]=0; // offset
			i++;
		}
	}
}

void kmp(int l1, int l2)
{
	// in real matching, i and j both start from 0.
	int i=0,j=0; // offset
	while(i<l1)
	{
		if(s1[i] == s2[j]) // if current character matches, continue matching
		{
			i++;
			j++;
			if(j==l2) // finished matching
			{
				cout<<i-l2<<endl;
				j = kmpnext[j-1];
			}
		}
		else if(j>0) // offset, if match is broken, move j back to the next possible position
		{
			j = kmpnext[j-1];
		}
		else //j = 0 and s1[i]!=s2[j]
		{
			i++;
		}
	}
}

int main()
{
	cin>>s1;
	cin>>s2;
	int l1 = strlen(s1);
	int l2 = strlen(s2);
	getkmpnext(l2);
	kmp(l1, l2);
}