# Real Small Water Problem

#### 题目描述

The senior wanted you to create a water problem.This made you a headache.So you asked BingYu for help.Immediately after he listened,he came up with a problem:


Give you a positive integer n.
Function F_x satisfies:
  F_(0) = sin{n}
  F_(x) = sin{F_(x-1)} (x>0)
Calculate F_(n).

#### 输入格式

The input contains no more than 20 test cases.


For each test case, the only line consists of one integer n.
0<=n<=100.

#### 输出格式

For each given n, print the answer in a single line.The result should be rounded to six decimal places.

#### 输入样例 复制

```plain
0
1
2
```

#### 输出样例 复制

```plain
0.000000
0.745624
0.709700
```

```python
import math
#from decimal import Decimal
def f(x,n):
    if x==0:
        return math.sin(n)
    elif n>0:
        return math.sin(f(x-1,n))
while True:
    n=float(input())
    m=n
    print("%.6f"%f(n,m))
```

