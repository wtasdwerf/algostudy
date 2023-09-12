# 음식물 피하기
</span>
<br>

> 출처 : https://www.acmicpc.net/problem/1743

<br/><br>

## 문제

> 코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다. 
>
> 이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다. 
>
> 통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 
>
> 선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.

<br/><br>

## 풀이

<br>

> 문제가 쉬우셨나요? bfs dfs 둘다 풀면서 연습 고고씽

<br/>

```python
# dfs 풀이

import sys
sys.setrecursionlimit(10000) # 재귀 깊게 해주는 코드

# 델타 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dfs
def dfs(x, y):
    visited[x][y] = 1
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx < n + 1 and 1 <= ny < m + 1:
            if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                dfs(nx, ny)


n, m, k = map(int, sys.stdin.readline().split())
arr = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    arr[r][c] = 1

result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            result = max(result, cnt)

print(result)
```
```python
# bfs 풀이

import sys
from collections import deque

# 델타 탐색
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# bfs
def bfs(x, y):
    cnt = 1
    que = deque([(x, y)])
    visited[x][y] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx < n + 1 and 1 <= ny < m + 1:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                    cnt += 1
    return cnt


n, m, k = map(int, sys.stdin.readline().split())
arr = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    arr[r][c] = 1


result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == 1 and visited[i][j] == 0:
            result = max(result, bfs(i, j))

print(result)
```






## 의문점
> 해결되지 않은 부분


<br/><br>


## 배운점
> TIL

