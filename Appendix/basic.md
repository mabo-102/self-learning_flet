# Python 基礎

- Python の基礎的なもの

## 入力

```py:文字列→整数
N = int(input())
N, M = [int(n) for n in input().split()]
A = [[int(n) for n in input().split()] for _ in range(N)]
B = [int(input()) for _ in range(M)]
```

```py:分割指定
# INPUT: 60 2 2 4
d = 1
C, A = [int(n) if i<d else [int(x) for x in n.split()] for i, n in enumerate(input().split(' ', d))]
# C: 60
# A: [2, 2, 4]
```

## 出力

```py:リストを1行ずつ改行して出力
[print(sum([x*y for x,y in zip(a, B)])) for a in A]
print('\n'.join(str(a) for a in range(1, 11)))
```

```py:リストを展開して出力
print(*[a for a in range(1, 11)])
print(' '.join(str(a) for a in range(1, 11)))
```

```py:20桁右詰め
C = [0, 0, 0, 0, 0, 0]
print('{:>20}'.format(' '.join([str(c) for c in C])))
print(' '.join([str(c) for c in C]).rjust(20))
```

```python:小数点以下の桁数を指定して出力
a = 2
b = 100000009

'{:.10f}'.format(a/b) # 0.0000000200
```

## 算数

### 余りを切り上げる

```python
a = 17
b = 3
(a+b-1) // b # 6
```

```python
import math

a = 17
b = 3
math.ceil(a / b) # 6
```

### 商と余りを取得する

```python
a = 5
b = 4
divmod(a, b) # (1, 1)
```

### 整数部と小数部を取得する

```python
import math

f = 3.1415
math.modf(f) # (0.14150000000000018, 3.0)
```

### 小数点以下が0か判定

```python
f = 2.0
f.is_integer() # True

f = 2.2
f.is_integer() # False
```

### 平方根(ルート)

```py
import math

x = 2
math.sqrt(x) # 1.4142135623730951
```

### 指数

```py
x = 2
x ** 0.5 # 1.4142135623730951
```

### 対数

```python
import math

math.e # 2.718281828459045

math.log(math.e) # 1.0

math.log10(100) # 2.0

math.log(100, 10) # 2.0
```

### 角度

```py
import math

theta = math.pi/2
math.degrees(theta) # 90.0

theta = 90
math.radians(theta) # π/2 -> 1.5707963267948966
```

## データ構造

### スタック

```python
stack = []
stack.append(1) # stack: [1]
stack.append(2) # stack: [1, 2]
x = stack.pop() # stack: [1] , x: 2
```

### キュー

```python
queue = []
queue.append(1) # queue: [1]
queue.append(2) # queue: [1, 2]
x = queue.pop(0) # queue: [2] , x: 1
```

### [deque](https://docs.python.org/ja/3/library/collections.html#collections.deque)

- Deque とは、スタックとキューを一般化したもの

```python
from collections import deque

l = [2, 5, 8]
d = deque(l)
try:
    d.append(9) # deque([2, 5, 8, 9])
    d.appendleft(1) # deque([1, 2, 5, 8, 9])
    d.pop() # 9
    d.popleft() # 1
    d.insert(1, 8) # deque([2, 8, 5, 8])
    d.count(8) # 2
    d.reverse() # deque([8, 5, 8, 2])
    d.index(8) # 0
    d.rotate(1) # deque([2, 8, 5, 8])
#    d.index(9) # IndexError
    d.remove(9) # ValueError
except (ValueError, IndexError) as e:
    print(e)
```

### 優先付きキュー

- [ABC141-D](https://atcoder.jp/contests/abc141/submissions/7613489)　M回最大値を取り出して処理をする。

```python
import heapq

A = [-int(n) for n in input().split()] # 通常は最小値がheap[0]になる。-で補正すればheap[0]に最大値。
heapq.heapify(A)
-heapq.heappop(A) # 取り出す際に符号を戻す。
```

## アルゴリズム

### 階乗

```python
from math import factorial

n = 3
factorial(n) # 6
```

### 順列

```python:重複なし
from itertools import permutations

n = 3
[p for p in permutations(range(1, n+1), n)] # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

```py:重複あり
from itertools import product

n = 2
[i for i in product(range(1, 4), repeat=n)] # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
```

### 組合せ

```python:重複なし
from itertools import combinations

n = 3
[c for c in combinations(range(1, n+1), 2)] # [(1, 2), (1, 3), (2, 3)]
```

```python:重複あり
from itertools import combinations_with_replacement

n = 3
[c for c in combinations_with_replacement(range(1, n+1), 2)] # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

```py:N個から2個取り出す組合せ
def nC2(n):
    return n * (n-1) // 2
```

### 素数判定

```python
def is_primenumber(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True 
```

### エラトステネスの篩

```python
def eratos(n):
    p = [2]
    l = list(range(3, n+1, 2))
    while l[0] < int(n**0.5)+1:
        p.append(l.pop(0))
        l = [x for x in l if x % p[-1]]
    return p + l
```

### Nの約数列挙

```py
import math
import heapq

N = 36
ans = [1, N]
heapq.heapify(ans)
for i in range(2, math.ceil(N**0.5)+1):
    if N%i == 0:
        heapq.heappush(ans, i)
        if i*i != N:
            heapq.heappush(ans, N//i)
print(*[heapq.heappop(ans) for _ in range(len(ans))])
# 1 2 3 4 6 9 12 18 36
```

### 公約数

```python
a = 8
b = 12
x = []
for i in range(1, min(a, b)+1):
    if a%i==0 and b%i==0:
        x.append(i) # [1, 2, 4]
```

### 最大公約数(gcd)

```python
import fractions
import math

a = 8
b = 12
fractions.gcd(a, b) # 4
math.gcd(a, b) # 4
```

### 最小公倍数

```python
# a = 8, b = 12
# x = gcd(a, b) # 4
# a = 2 * x, b = 3 * x
# すなわち、最小公倍数は、a * b // x
# ちなみに、素数同士ならx = 1なので a * b
import fractions　# <3.7
import math # >=3.7

a = 8
b = 12
a * b // math.gcd(a, b) # 24
a * b // fractions.gcd(a, b) # 24 
```

### 累積和

- N個の中から隣接するK個の和の最大値を求める場合

```python
import itertools

N, K = [int(n) for n in input().split()]
P = [(int(n)+1)/2 for n in input().split()] # 期待値の計算
S = [0]+[E for E in itertools.accumulate(P)] # 累積和の計算
ans = 0
for j in range(N-K+1): # 最大値の計算
    ans = max(ans, S[j+K]-S[j])
print(ans)
```

### 二分探索法

```python
from bisect import *

A = [1, 3, 5, 5, 7, 9]
bisect(A, 2) # 1
bisect_left(A, 5) # 2
bisect_right(A, 5) # 4
```

### 再帰関数の実行上限解除

```python
import sys
sys.setrecursionlimit(10**7)
```

### 4300桁数制限解除

```python
import sys
sys.set_int_max_str_digits(0)
```
