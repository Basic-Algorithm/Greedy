#include <iostream>
#include <algorithm>
#include <string>

#define MUL_HOUR_CASE 3600
#define MUL_MIN_CASE  900
#define MUL_SEC_CASE  675

using namespace std;

int N;

int main()
{
	cin >> N;

	int ret = 0;

	if (N < 3)
	{
		ret = (N + 1) * (MUL_MIN_CASE + MUL_SEC_CASE);
	}
	else if (N < 13)
	{
		ret = N * (MUL_MIN_CASE + MUL_SEC_CASE) + MUL_HOUR_CASE;
	}
	else if (N < 23)
	{
		ret = (N - 1) * (MUL_MIN_CASE + MUL_SEC_CASE) + MUL_HOUR_CASE * 2;
	}
	else
	{
		ret = (N - 2) * (MUL_MIN_CASE + MUL_SEC_CASE) + MUL_HOUR_CASE * 3;
	}
	cout << ret;
}

//if 3, 13, 23h : 3600
//else if xh 3 13 23 30~39 43 53m : 60
//else xh xm : 3 13 23 30~39 43 53s