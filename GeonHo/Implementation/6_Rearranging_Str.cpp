#include <iostream>
#include <algorithm>

using namespace std;

string str;

int main()
{
	cin >> str;

	sort(str.begin(), str.end());

	int pos = 0;
	int sum = 0;

	for (; pos < str.size(); pos++)
	{
		if ((int)str[pos] > 58) break;

		sum += (int)str[pos] - '0';
	}

	cout << sum << str.erase(0, pos);
}

/*
string str;
vector<char> result;
int value = 0

int main(void)
{
	cin >> str;

	for(int i = 0; i < str.size(); i++)
	{
		if(isalpha(str[i]))
		{
			result.push_back(str[i]);
		}
		else value += str[i] - '0';
	}

	sort(result.begin(), result.end());

	for (int i = 0; i < result.size(); i++) cout << result[i];
	
	cout << value;
}

*/