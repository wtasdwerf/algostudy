<br/><Br>

<span style = "color:orange">

# 블랙 프라이데이
</span>
<br>

> 출처 : https://www.acmicpc.net/problem/18114


<br/><br>

## 문제

> 서강 백화점이 블랙 프라이데이를 맞아서 특별 이벤트를 진행한다. 백화점에서 제시하는 양의 정수의 무게 C에 딱 맞게 물건들을 가져오면 전부 만 원에 판매하는 이벤트이다.

선택할 수 있는 물건은 최대 3개까지이고, 같은 물건을 중복 선택하는 것은 불가능하다. 그리고 백화점에서 판매하는 물건들의 무게는 모두 다르다.

예를 들어, 백화점에서 판매하고 있는 물건 5개의 무게가 각각 1, 2, 3, 4, 5일 때, C가 5라면 {2, 3} 또는 {5}에 해당하는 물건의 조합을 만 원에 구매할 수 있다.

판매하는 물건 N개의 양의 정수의 무게가 각각 주어질 때, 만 원에 구매할 수 있는 조합이 있는지 출력하라.

<br/><br>

## 풀이

```python
import sys
input = sys.stdin.readline


def binary_s(x, y, goal):
    while x <= y:
        mid = (x + y) // 2
        if weights[mid] == goal:
            return 1

        elif weights[mid] > goal:
            y = mid - 1

        else:
            x = mid + 1

    return 0


def bs():
    if c in weights:
        print(1)
        exit()

    i, j = 0, n - 1
    while i < j :
        a, b = weights[i], weights[j]
        if a + b > c:
            j -= 1

        elif a + b == c:
            print(1)
            exit()

        elif a + b < c:
            d = c - (a + b)
            if d != weights[i] and d != weights[j] and binary_s(goal=d, x=i, y=j):
                print(1)
                exit()
            i += 1

    return 0



n, c = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
#
# for i in range(n):
#     if weights[i] == c:
#         print(1)
#         exit()
#
#     elif weights[i] > c:
#         weights = weights[:i]
#         break


if not bs():
    print(0)
```
<br>



<br/><br>


## 의문점
> 해결되지 않은 부분


<br/><br>


## 배운점
> TIL

