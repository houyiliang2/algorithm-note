# ACM罚时

#### 题目描述

作为一个ACMer，总是习惯于在比赛中或比赛结束后查看自己的排名（Standing），有细心的同学发现Penalty（罚时），在相同做题数下Penalty越小越好（真是个令人振奋的发现）。让我们看看Penatly的计算方法：每道试题用时将从竞赛开始到试题解答被判定为正确（AC）为止，其间每一次提交运行结果被判错误的话将被加罚20分钟时间，未正确解答的试题不记时。例如：A、B两队都正确完成两道题目，其中A队提交这两题的时间分别是比赛开始后1:00和2:45，B队为1:20和2:00，但B队有一题提交了2次。这样A队的Penalty为1:00+2:45=3:45而B队为1:20+2:00+0:20=3:40，所以B队因Penalty少而获胜。当然如果你AC了某道题后，之后这一题所有提交的代码都不算罚时和时间（有时我也这么无聊~）。恰逢北化周一晚的周赛，在九楼机房18:00-22:00，考验随之而来——现在需要你计算大家的Penalty，Penalty初始为00:00，相信作为北化的ACMer相信你一定可以的！

#### 输入格式

输入包含多组数据，每组数据的第一行包含一个正整数N（1=<N<=20）表示此ACMer的提交次数，接下来的第2到N+1行表示每次提交的状态，由三个字段组成，第一个字段为一个整数A，表示当前的时间：hour:minutes（保证18=<hour<=22,0<=minutes<=60），第二个字段为一个大写字母（A~Z），表示题号，第三个字段表示OJ返回的状态，假设只可能是AC，WA，RE，TLE中的一种，均为大写

#### 输出格式

输出这位ACMer的Penalty，每个测试数据占一行

#### 输入样例

3
18:05 A RE
19:11 A AC
20:00 B WA
1
20:27 F AC

#### 输出样例

01:31
02:27

```c++
#include<iostream>
using namespace std;

struct Penalty//罚时结构体 
{
	int hour;//罚时的小时数 
	int minute;//罚时的分钟数 
};
int main()
{
	int N, m;
	int hour, minute;
	string s;	//OJ状态变量
	char q;		//题目号的变量
	while (cin >> N)//输入N组数据 
	{
		int AC[24] = { 0 };//判断是否AC数组 
		int pen[24] = { 0 };//罚时个数数组，每一个代表20分钟 
		Penalty penalty;
		penalty.hour = 0;//初始化 
		penalty.minute = 0;//初始化 
		while (N--)
		{
			cin >> hour;
			cin.get();//把冒号读走 
			cin >> minute;//读取分钟数 
			cin >> q;//读取题目号 
			cin >> s;//读取OJ返回的状态 
			m = q - 'A';
			if (!AC[m])//判断当前题目是否AC 
			{
				if (s == "AC")
				{
					penalty.hour += hour - 18;
					penalty.minute += minute;
					AC[m] = 1;
				}
				else
					pen[m]++;
			}
		}
		for (int i = 0; i < 24; i++)//把已经AC的题目的罚时时间加到总时间里面 
			if (AC[i])
				penalty.minute += pen[i] * 20;
		penalty.hour += penalty.minute / 60;
		penalty.minute %= 60;
		printf("%02d:%02d\n", penalty.hour, penalty.minute);
	}
	return 0;
}

```

