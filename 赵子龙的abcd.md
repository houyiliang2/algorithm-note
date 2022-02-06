# 赵子龙的abcd



#### 题目描述

今天，赵子龙在愉快地刷题时，碰到了这样一道题：
给出非负正数a,b,c,d，求a+b+c+d；
赵子龙：？？？？这么简单？？？？
现在，就请你帮组赵子龙刷掉这道简单题吧。

#### 输入格式

第一行，测试数组组数T（T<100）
对于每一组数据，都有四个非负正数a,b,c,d(0<=a,b,c,d<=2^62)

#### 输出格式

a+b+c+d的值

#### 输入样例 复制

```plain
2
0 0 0 0
1 1 1 1
```

#### 输出样例 复制

```plain
0
4
```

```c++
#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        unsigned long long a,b,c,d;
        cin>>a>>b>>c>>d;
        unsigned long long x=4611686018427387904;
        if(a==x&&b==x&&c==x&&d==x)
        {
            cout<<"18446744073709551616"<<endl;
        }
        else
        {
            cout<<a+b+c+d<<endl;
        }
    }
    return 0;
}

```

```python
n = int(input())
x = 4611686018427387904
while n:
    a , b , c , d = input('').split()
    if a==x and b == x and c == x and d == x:
        print('18446744073709551616')
    else:
        print(int(a)+int(b)+int(c)+int(d))
```

