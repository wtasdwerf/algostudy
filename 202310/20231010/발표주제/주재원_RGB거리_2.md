<br/><Br>

<span style = "color:orange">

# RGB거리 2
</span>
<br>

> 출처 : https://www.acmicpc.net/problem/17404


<br/><br>

## 문제

> RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

## 입력

> 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

## 출력

> 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

<br/><br>

## 풀이

```python
  N = int(input())

  # 색칠 비용값
  rgb = [list(map(int,input().split())) for _ in range(N)]

  # INF 설정
  ans = I = 1e9

  # 행 전체
  for i in range(3):

      # dp가 각 R, G, B로 시작했을 때
      dp = [[I,I,I] for _ in range(N)]

      # 처음 집 색칠
      dp[0][i] = rgb[0][i]

      # 2번째 집부터 R, G, B로 색칠했을 때 최소값 갱신
      for j in range(1,N):
          dp[j][0] = rgb[j][0] + min(dp[j-1][1],dp[j-1][2])
          dp[j][1] = rgb[j][1] + min(dp[j-1][0],dp[j-1][2])
          dp[j][2] = rgb[j][2] + min(dp[j-1][0],dp[j-1][1])

      for k in range(3):
          # 첫번째 집과 N번째 집이 다른 경우만 선택
          if i != k:
              ans = min(ans,dp[-1][k])
  print(ans)
```
<br>

> 풀이설명

rgb에 각 집별로 RGB 색칠할 때의 비용을 입력받습니다. 
ans는 최소비용을 매우큰 값으로 초기화하고, I는 무한대의 개념으로 매우 큰값으로 초기화해줍니다. 
for문을 i로 돌며 첫 번째 줄에 있는 값들을 첫 dp로 정합니다.
첫번째 집을 색칠하고 두번째 줄 이후의 집부터는 for문을 j로 돌며 i와 다른 값을 가지는 열에 해당하는 값 중 최솟값을 구하면서 집을 각각 R, G, B로 색칠했을 때의 최소비용을 갱신해 나갑니다. 
for문을 k로 돌며 첫 번째 집과 마지막 집의 색깔이 서로 다른 경우만 ans에 최솟값으로 갱신해 줍니다.


## 의문점
> 해결되지 않은 부분


<br/><br>


## 배운점
> TIL

