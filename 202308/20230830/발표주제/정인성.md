<br/><Br>

<span style = "color:orange">

# A형 2번 기지국 건설

### 기억복원이라 조건이 부족할수도 있는데 최대한 기억해서 필요한 조건을 적어봤습니다

### 28일 시험때 기억나시는대로 최대한 풀어주세요! 

### 헷갈리는 점 있으면 저한테 문의주시면 감사하겠습니다~!

### input 데이터, output 데이터는 문제 마지막에 넣어놨습니다.







> 출처 : 삼성SW역량테스트 A형 (문제작성 : 인성's brain memory) (주의 - 하루지난 기억임) 



## 문제

> KBS는 기지국이 부족한 지역을 발견해 최대의 이익을 얻을 수 있도록 기지국 4개를 추가로 건설하려고 한다.
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
> --
> 입력은 첫번째 줄에 테스트 케이스 수 T가 주어진다 (1 <= T <= 10)
>
> 두번째줄은 테스트케이스별로 행(H)의 개수와 열(W)의 개수가 W H 형태로 들어간다
>
> 이후에 H줄에 걸쳐 W개의 기지국 별 사용자에 대한 정보가 주어진다



### 입출력 데이터

>  [input.txt](..\..\PycharmProjects\pythonProject\ALGO\230829 알고\A_1\input.txt)
>
>  [output.txt](..\output.txt) 



### 풀이

```python
import sys
sys.stdin = open('input.txt')

def dfs(x, y, cnt):
    global ans
    if visited[x][y] == 4:
        if cnt > ans:
            ans = cnt
        visited[x][y] = 0
        return
    # 열에 따라 다른 델타 탐색 위치
    if y % 2 == 1:
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [1, 1]]:
            nx = i + x
            ny = j + y
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, cnt + arr[nx][ny])
    else:
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1]]:
            nx = i + x
            ny = j + y
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, cnt + arr[nx][ny])


def delta(x,y):
    global ans
    cnt = arr[x][y]
    zone = []
    if y % 2 == 1:
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [1, 1]]:
            nx = i + x
            ny = j + y
            if 0 <= nx < H and 0 <= ny < W:
                zone.append(arr[nx][ny])
    else:
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1]]:
            nx = i + x
            ny = j + y
            if 0 <= nx < H and 0 <= ny < W:
                zone.append(arr[nx][ny])

    num = 3
    while num != 0:
        if not zone:
            break
        cnt += max(zone)
        zone[zone.index(max(zone))] = 0
        num -= 1

    if cnt > ans:
        ans = cnt




T = int(input())
for tc in range(1, T+1):
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = 0

    # dfs 돌려서 4개 이익과 현재위치 3개붙어있는거 비교해서 최댓값 출력

    for i in range(H):
        for j in range(W):
            visited = [[0] * W for _ in range(H)]
            visited[i][j] = 1
            # dfs
            dfs(i, j, arr[i][j])
            # 1-3 구조
            delta(i,j)


    print(f'#{tc} {ans**2}')
```



>  
