#include <iostream>

using namespace std;

string str;

int main()
{
	cin >> str;

	float cnt_change = 0;
	char lastLetter = str[0];

	for (int i = 1; i < str.length(); i++)
	{
		if (str[i] == '0' && lastLetter == '1')
		{
			lastLetter = '0';
			cnt_change++;
		}
		else if (str[i] == '1' && lastLetter == '0')
		{
			lastLetter = '1';
			cnt_change++;
		}
	}

	cout << ceil(cnt_change / 2) << endl;
}

/*
* 尻紗吉 収切研 乞砧 廃腰拭 及増澗依戚 置社 獣楳聖 幻糾生稽 益軒巨 硝壱軒葬 紫遂
* 0引 1税 帰嬢軒研 唖唖 し, け虞 馬檎 衣厩 壕伸税 莫殿澗 しけしけしけし...
* し -> け && け -> し稽 痕莫鞠澗 獣繊聖 count
* 痕莫鞠澗 乞窮 獣繊聖 姥廃 板 count /2 馬食 置社 獣楳 判呪 窒径
*/