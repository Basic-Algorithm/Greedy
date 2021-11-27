//#include <iostream>
//
//using namespace std;
//
//string N;
//
//int main()
//{
//	cin >> N;
//	int length = N.size();
//	int left_score = 0, right_score = 0;
//
//	for (int i = 0; i < length / 2; i++)
//		left_score += N[i];
//
//	for (int i = length / 2; i < length; i++)
//		right_score += N[i];
//
//	if (left_score == right_score)
//		cout << "LUCKY";
//	else
//		cout << "READY";
//}