<br/><Br>

<span style = "color:orange">

# Ignition
</span>
<br>

> 출처 : [링크](https://www.acmicpc.net/problem/13141)


<br/><br>

## 문제

> 서훈이는 오늘 있었던 알고리즘 과목 기말고사를 망쳐서 기분이 좋지 않다. 서훈이는 스트레스도 풀 겸 시험 문제로 나온 그래프를 불로 태우려고 한다.



서훈이는 그래프의 정점 (위 그림에서 동그라미로 표시된 곳) 중 한 곳에 불을 붙일 수 있다. 정점에 불이 붙으면 곧바로 노드와 연결된 간선을 따라서 불이 전달된다. 간선 위에서는 불은 1초당 1만큼의 거리를 이동한다. 만약 어떤 간선의 양 끝 정점에 불이 붙은 경우 불은 간선의 중앙까지 태운 후 꺼진다.

서훈이는 그래프를 최대한 빠른 시간 안에 전부 태우고 싶어한다. 서훈이를 도와 어떤 정점에 불을 붙일지 구하는 프로그램을 작성하여라. 단, 위 그림에서 간선끼리 교차하는 것은 무시한다.
<br>

입력
첫 번째 줄에는 그래프의 정점의 수 N과 간선의 수 M이 주어진다. (2 ≤ N ≤ 200, N-1 ≤ M ≤ 20,000)

두 번째 줄부터 M개의 줄에는 각 간선의 시작점 S, 끝점 E, 길이 L이 주어진다. (1 ≤ L ≤ 100)

시작점과 끝점이 같은 간선도 있을 수 있으며, 특정 두 정점을 직접 연결하는 간선의 수가 여러 개일 수 있다. 또한, 그래프의 모든 정점들은 간선들을 통해서 연결되어 있다.
<Br>
출력
주어진 그래프를 모두 태우는 데 걸리는 최소 시간을 출력한다. 답은 소수점 아래 한 자리까지 출력한다. 문제의 특성 상 오차가 생길 일이 없으므로 출력 데이터와 정확히 일치해야 정답으로 처리한다.

<br/><br>

## 풀이

```python
import sys
import heapq
input = sys.stdin.readline


def dijkstra(s):
    pq = []
    heapq.heappush(pq, (s, 0))
    distances[s] = 0

    while pq:
        cur_node, dist = heapq.heappop(pq)

        if distances[cur_node] < dist:
            continue

        for next in graph[cur_node]:
            next_node = next[0]
            next_dist = next[1]

            total_dist = dist + next_dist

            if distances[next_node] > total_dist:
                distances[next_node] = total_dist
                heapq.heappush(pq, (next_node, total_dist))


n, m = map(int, input().split())    # 정점의 수, 간선의 수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, l = map(int, input().split())  # 간선의 시작, 끝, 길이
    graph[s].append((e, l))     # 노드, 가중치
    graph[e].append((s, l))
# print(graph)

result = []
for i in range(1, n + 1):
    distances = [1e9 for _ in range(n + 1)]
    dijkstra(i)     # 모든 정점에 대해 수행

    times = []
    for j in range(1, n + 1):   # 그래프에 접근
        for k in range(len(graph[j])):  # 그래프의 j번노드의 인접 리스트에 접근
            node1, node2, dist = j, graph[j][k][0], graph[j][k][1]
            time1, time2 = distances[node1], distances[node2]   # 각 노드에 불 붙는 시각
            # 간선이 모두 불타는 시각
            temp = min(time1, time2) + abs(time1 - time2) + ( (dist - abs(time1 - time2)) / 2)
            times.append(temp)

    result.append(max(times))

print(min(result))
```
<br>

> 풀이설명

> 1. 각 그래프의 모든 정점에 대해 다익스트라 수행  
> 2. 그래프의 정점에서 각 노드의 최소 거리를 distances에 저장  
>     1) distances의 각 인덱스에 담긴 값은 i번 노드에서 점화되었을때 각 인덱스 노드에 불이 붙는 시각  
> 3. graph에 담긴 모든 간선에 접근  
> 4. graph의 간선에 접근하면, 각 간선의 양 끝 노드와 가중값을 먼저 추출하고 distances에서 양 끝 노드에 불이 붙는 시각을 추출  
> 5. 간선이 모두 타는 **시각**을 계산하여 추출  
> 6. 간선이 모두 타는 **시각** 중 가장 큰 값이 그래프 전체가 탄 시각이므로, max로 추출하여 result에 삽입
> 7. 2 ~ 6의 과정을 시작점을 바꿔가며 모두 다시 수행하며 result에서 가장 작은 값을 추출
<br/><br>


## 의문점
> 해결되지 않은 부분


<br/><br>


## 배운점
> TIL

