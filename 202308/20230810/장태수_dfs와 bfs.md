<br/><Br>

<span style = "color:orange">

# DFS와 BFS
</span>
> 출처 : https://www.acmicpc.net/submit/1260/63936349

## 문제

> 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.


## 풀이

```python
    from collections import deque


def dfs(graph, start, visited):
    # 현재 노드의 방문처리
    visited[start] = True
    print(start, '', end='')

    # 현재 노드와 연결된 노드에 재귀함수를 활용해서 방문해주기
    for i in graph[start]:
        # 방문하지 않은 노드라면 해당 노드로 dfs 실행
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    # queue 활용
    queue = deque([start])
    # 현재 위치한 노드는 방문처리
    visited[start] = True
    # 큐가 빌때까지 큐에서 하나의 원소를 뽑아서 출력
    while queue:
        popped = queue.popleft()
        print(popped, '', end='')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[popped]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


'''
1. 경로 탐색을 위해 필요한 각 노드당 연결된 노드들의 리스트 작성
2. 각 노드를 방문했는지 확인하는 리스트 작성
3. dfs, bfs 돌리기

    1) dfs(깊이 우선 탐색)
    - '현재 노드'를 기준으로 가까운 노드를 탐색
    - 1. 현재 노드의 방문처리
    - 2. 현재 노드와 연결된 다른 노드를 재귀로 방문
    
    2) bfs(넓이 우선 탐색) * deque를 활용
    - '시작점'을 기준으로 가까운 노드를 탐색
    - 1. 현재 노드의 방문처리
    - 2. 큐가 빌때까지, 큐에서 하나의 원소를 뽑아 출력
    - 3. 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    
'''

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
n, m, start = map(int, input().split())

# 1의 과정
graph = list([] for _ in range(n+1))

# 1의 graph에 추가할 노드들
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 2의 과정 (방문 시 True로 변경)
visited = [False] * (n + 1) # dfs에서 활용할 리스트
visited2 = [False] * (n + 1) # bfs에서 활용할 리스트

# 통상적인 경우, 숫자가 작은 노드를 먼저 방문하므로 graph의 각 행을 오름차순 정렬
for row in graph:
    row.sort()

# 3의 과정

dfs(graph, start, visited)
print()
bfs(graph, start, visited2)


```
<br>

> 풀이설명

dfs 와 bfs의 기본적인 동작원리를 이해하고 있는지 물어보는 문제


## 의문점
> dfs, bfs의 실무 활용처


<br/><br>


## 배운점
> 해당 코드를 작성하면서 dfs, bfs의 개념을 더 단단히 다지는 계기가 되었다.

