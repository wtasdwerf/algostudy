# 김범수

# N-Queen

> 출처 : [https://www.acmicpc.net/problem/9663](https://www.acmicpc.net/problem/9663)
> 

## 문제

> N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
> 
> 
> N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
> 

## 풀이

```python
# N-Queen
def nQueen(N, r, pos):
    # 끝까지 오면 성공
    if r == N:
        return 1
        
    ret = 0
    for c in range(N):
        for i in range(r):
            # 다른 퀸의 경로를 가로막으면 해당 칸은 둘 수 없으므로 break
            if pos[i]-c == 0 or pos[i]-c == r-i or pos[i]-c == i-r:
            break
        else: # 다른 퀸을 가로막지 않으면 해당 칸에 둘 수 있음
            pos[r] = c
            ret += nQueen(N, r+1, pos)
    return ret
    
print(f'{nQueen(int(input()), 0, [-1 for _ in range(14)])}')
```

> 백트래킹을 사용해서 해결한다. 행별로 하나씩 두면서 둘 수 없는 칸은 그 이상 담색을 하지 않고 다음칸을 확인한다.
> 

## 의문점

## 배운점

> TIL
>