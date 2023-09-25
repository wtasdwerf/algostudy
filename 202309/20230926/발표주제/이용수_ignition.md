# 김범수

# **Ignition**

> 출처 : [https://www.acmicpc.net/problem/13141](https://www.acmicpc.net/problem/13141)
> 

## 문제

서훈이는 그래프의 정점 (위 그림에서 동그라미로 표시된 곳) 중 한 곳에 불을 붙일 수 있다. 정점에 불이 붙으면 곧바로 노드와 연결된 간선을 따라서 불이 전달된다. 간선 위에서는 불은 1초당 1만큼의 거리를 이동한다. 만약 어떤 간선의 양 끝 정점에 불이 붙은 경우 불은 간선의 중앙까지 태운 후 꺼진다.

서훈이는 그래프를 최대한 빠른 시간 안에 전부 태우고 싶어한다. 서훈이를 도와 어떤 정점에 불을 붙일지 구하는 프로그램을 작성하여라. 단, 위 그림에서 간선끼리 교차하는 것은 무시한다.

## 풀이

```python
import sys, heapq
sys.stdin = open('input.txt')

# 다익스트라를 돌려서 모든 정점까지 닿는 최소 거리를 구한다
def djk(start):
    heap = []
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    while heap:
        w, cur = heapq.heappop(heap)
        for next in graph[cur]:
            next_v = next[0] + w
            next_i = next[1]
            if visited[next_i] > next_v:
                visited[next_i] = next_v
                heapq.heappush(heap, (next_v, next_i))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    S, E, L = map(int, input().split())
    graph[S].append((L, E))
    graph[E].append((L, S))

max_v = 0
min_v = 1e9
result = []

for i in range(N+1):
    visited = [1e9]*(N+1)
    djk(i)
    max_v = 0
    # 두개의 노드가 불타는 시간을 각각 left, right 로 저장한다
    for k in range(len(graph)):
        for j in range(len(graph[k])):
            temp = 0
            left = visited[k]
            right = visited[graph[k][j][1]]
            cur = graph[k][j][0]
            # 디버그
            if left == 1e9 or right == 1e9:
                continue
            # 양쪽 시간을 비교해서 간선이 타는 시간을 구해준다
            if left > right:
                temp = left + (cur - (left-right)) / 2
            elif right > left:
                temp = right + (cur - (left+right)) / 2
            elif left == right:
                temp = left + cur / 2
            # 해당 턴에 가장 늦게 간선이 타는 시간을 구해준다
            max_v = max(max_v, temp)
    # 디버그
    if max_v == 0:
        continue
    # 모든 최종 간선이 타는 시간들을 취합해서 최소값을 구해주고 해당 시간을 출력해주면 끝!
    min_v = min(max_v, min_v)
print(min_v)

```

### 힌트

- 각 정점이 불이 붙기 시작한 시간은 우리가 배운 알고리즘으로 구할 수 있다.
- 각 간선이 다 타는 시각은 각 정점에 불이 붙기 시작한 시간을 이용해서 구할 수 있다.

## 의문점

## 배운점

> TIL