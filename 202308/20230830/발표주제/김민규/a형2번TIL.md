<br/><Br>

<span style = "color:orange">

# 문제 제목
</span>
<br>

> 출처 : 정인성님 머릿속, 그리고 우리의 마음속..


<br/><br>

## 문제

> > KBS는 기지국이 부족한 지역을 발견해 최대의 이익을 얻을 수 있도록 기지국 4개를 추가로 건설하려고 한다.
>
> 이용자가 많을수록 최대의 이익을 얻을 수 있으므로 이용자가 가장 많도록 기지국을 건설한다.
>
> 또한 4개의 기지국은 모두가 인접해있어야 원활히 작동한다. 
>
> (두개씩 인접해있고 두 그룹이 떨어져있다면 원활히 작동하지 않는다, 1개만 떨어져있고 3개가 붙어있어도 원활히 작동하지 않는 것은 마찬가지이다)
> 
>
> 기지국이 최대로 얻을 수 있는 이익을 계산하는 프로그램을 작성하시오.
>
> - 이익 계산법 = (기지국1 사용자 +기지국2 사용자 +기지국3 사용자 +기지국4 사용자)^2
>
> 
>
> 조건)
>
> 1. 기지국은 4개를 건설한다.
>
> 2. 4개의 기지국은 각각 최소 한개이상의 기지국과 인접해 있고, 모든 기지국은 인접해있다.
>
> 3. 건설된 기지국이 있는 위치에 사용하는 사용자수가 최대가 되도록 기지국을 건설해야 기지국은 최대의 이익을 볼 수 있다
>
> 4. 홀수인 열은 12시, 3시, 6시, 9시, 5시, 7시 행렬과 인접해있고, 짝수인 열은 상하좌우 12시, 3시, 6시, 9시, 11시, 1시 행렬과 인접해있다
>
>    (벌집모양 표현 못하겠어서 이렇게 해석해서 조건으로 적었습니다~~!)
>

입력

> 첫번째 줄에 테스트 케이스 수 T가 주어진다 (1 <= T <= 10)
>
> 두번째줄은 테스트케이스별로 행(H)의 개수와 열(W)의 개수가 W H 형태로 들어간다
>
> 이후에 H줄에 걸쳐 W개의 기지국 별 사용자에 대한 정보가 주어진다


<br/><br>

## 풀이

```python
# A형 2번
T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split()) # 주어지는 기지국들의 행/열 크기
    arr = [list(map(int, input().split())) for _ in range(N)] # 기지국별 유저 수

    odd_d = [[-1, 0], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]] # i가 odd일 때의 방향
    even_d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0]] # i가 even일 때의 방향
    
    result1 = 0 # 별자리 모양 기지국
    result1_idx = []
    result2 = 0 # 불가사리 모양 기지국
    result2_idx = []
    # 각 요소 별로 연결되는 4개의 기지국 유저 합의 제곱중 최대값을 구한 후,
    # 해당 최대값을 기존 최대값과 비교
    for i in range(N):
        for j in range(M):

            # 1. bfs
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            queue = [[[i, j]]]

            while queue:
                now = queue.pop(0)
                ni, nj = now[0][0], now[0][1]

                # if visited[ni][nj] > 4:
                    # break

                if ni%2: # 현재 행이 odd인 경우
                    dir = odd_d
                else: # 현재 행이 even인 경우
                    dir = even_d

                # 1. 본인 기준 쭉쭉 뻗어나가기
                for di, dj in dir:
                    if 0 <= ni + di < N and 0 <= nj + dj < M and visited[ni+di][nj+dj] == 0:
                        visited[ni+di][nj+dj] = visited[ni][nj] + 1
                        new = [[ni+di, nj+dj]] + now
                        if len(new) == 4:
                            # print(new, end = ' ')
                            c = 0
                            for y, x in new:
                                c += arr[y][x]
                            if result1 < c:
                                result1 = c
                                result1_idx = new
                        else:
                            queue.append(new)
                            ni += di
                            nj += dj
   # 2. 불가사리 구조
    for i in range(N):
        for j in range(M):

            if i%2: # 홀수인 경우
                dir = odd_d
            else: # 짝수인 경우
                dir = even_d
            # 시작 인덱스값 추가
            c = arr[i][j]
            adjs = [] # 인접한 인덱스를 담을 배열
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    adjs.append(arr[ni][nj])
            adjs.sort(reverse = True) # 큰 값이 앞에 오게끔 정렬

            # 인접 요소가 3개 이상 있을 시, 기지국 건설 가능
            if len(adjs) >= 3:
                # 가장 사용자가 많은 3개의 기지국 선택 후 +
                for k in range(3): 
                    c += adjs[k] 
                if result2 < c:
                    result2 = c
                    result2_idx = new
            
    print(result1, result2)
    print(result1_idx, result2_idx)
```
<br>

> 하나의 (i, j)쌍으로부터 인접한 3개의 기지국을 골라서 4개의 연결된 기지국을 건설하는 두 가지 방법에 대해 고민
> 1. 별자리 모양 -> 각 i, j에서 다음 나아갈 방향을 적절히 고르는 방법
> 2. 불가사리 모양 -> i, j의 인접 요소들 중 가장 큰 사용자를 보유하고 있는 3개의 기지국을 선택하는 방법

<br/><br>


## 의문점
> 1번 방법(별자리모양 기지국 건설)을 활용하는 데에 bfs를 활용하여 각 자리별로 행의 홀/짝을 판단한 후 주변을 탐색하는 방법을 선택했는데, 결과가 제대로 나오지 않는 것 같다.
> 특히, 처음 시작점의 근처에서 갇혀서 돌아가는 듯 하다. 이를 해결하기 위한 방안을 마련하고 싶다.


<br/><br>


## 배운점
> TIL

