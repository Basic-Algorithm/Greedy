#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

int N, K;
vector<int> arr_A;
vector<int> arr_B;

void Initialize();

int main()
{
	Initialize();

	sort(arr_A.begin(), arr_A.end());
	sort(arr_B.begin(), arr_B.end(), greater<>());

	for (int i = 0; i < K; i++)
	{
		if (arr_A[i] > arr_B[i]) break;

		arr_A[i] = arr_B[i];
	}

	cout << accumulate(arr_A.begin(), arr_A.end(), 0);
}

void Initialize()
{
	cin >> N >> K;

	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		arr_A.push_back(x);
	}

	for (int i = 0; i < N; i++)
	{
		int x;
		cin >> x;
		arr_B.push_back(x);
	}
}