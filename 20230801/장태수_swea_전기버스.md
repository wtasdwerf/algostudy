<br/><Br>

<span style = "color:orange">

# 문제 제목
</span>
<br>

> 출처 : https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AYYUhZfqIYADFARc&probBoxId=AYmbBU3a7c0DFAUe&type=USER&problemBoxTitle=PRACTICE&problemBoxCnt=6


<br/><br>

## 문제

> A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.



 


[예시]

![Alt text](..\20230801\장태수_img\08011.png)

다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.

 

[입력]
 

첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 

[출력]


#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

<br/><br>

## 풀이

```python
   import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T + 1):
    # 한번 충전으로 이동가능한 거리, 정류장 수, 충전기가 설치된 정류장의 개수
    k, n, m = map(int, input().split())
    # 충전기가 설치된 정류장의 위치
    charges = list(map(int, input().split()))

    # 어디서 충전하는지 알 필요 없음. 몇번 충전해야 하는지 관건
    charge_cnt = n // k

    # 역들의 상태 확인을 위해 인덱스가 역의 번호, 값이 충전기 설치여부를 나타내는 배열 생성
    station = []
    for j in range(n+1):
        if j in charges:
            station.append(1)
        else:
            station.append(0)

    possible = True

    # 배터리의 잔량 확인
    battery = k
    # 충전 횟수 확인
    cnt = 0
    # 충전기 모음의 인덱스
    charges_idx = 1

    # station의 인덱스를 기준으로 진행
    for x in range(1, n):

        # 배터리 잔량 확인
        if battery >= 0:
            # 정류장에 충전소가 없는 경우
            if station[x] == 0:
                battery -= 1

            # 정류장에 충전소가 있는 경우
            elif station[x] == 1:
                # 마지막 충전소 정거장인 경우 종점까지 갈 수 있는지 판단
                if x == charges[-1]:
                    # 배터리의 용량 - 종점까지 남은 정거장의 수
                    if battery - (n - x) >= 0:
                        continue

                    else:
                        possible = False
                        break

                # 다음 충전소가 있는 정류장까지 갈수 없으면 충전. charges[charges_index]로 다음
                # 충전소가 있는 정거장의 위치를 받아올 수 있음
                elif battery - charges[charges_idx] < 0:
                    # 배터리의 충전
                    battery = k
                    # 다음 충전소 방문을 위해 인덱스 값 1 증가
                    charges_idx += 1
                    # 충전 횟수 증가
                    cnt += 1

        # 배터리가 0미만인 경우 진행 불가
        else:
            possible = False
            break

    # 진행 가능 여부 판단
    if possible:
        print(f"#{i}", cnt)

    else:
        print(f"#{i}", 0)

```
<br>

> 풀이설명  
> 
    전기 버스의 정방향 진행에 있어 각 정거장마다 모든 상황을 파악하려 하는 구문이다.
    각 정거장마다 충전소 유무를 확인하고, 버스의 배터리 잔량을 확인하며, 충전소 보유 정거장 중 마지막에 도달하는 경우에 종점까지 갈 수 있는지 판단하고 갈 수 없다면 불가능하다고 판단하여 possible에 False를 할당하여 불가능으로 변경

<br/><br>


## 의문점
> 범수의 역추적 접근 발상 관련해서 이해하고 싶음 (왜 역추적을 활용하려 했을까?)  
>  
> 더 코드를 간결하게 구성할 수 없을까?  
> 
> 다른 사람의 풀이는 간결하고 나의 풀이가 더 길고 복잡한 이유는?



<br/><br>


## 배운점
> 스스로 처음으로 스터디를 구성해서 첫 날 스터디에 준비가 많이 부족했다. 다른 사람들도 이해할 수 있게 더 이해하기 쉬운 주석 작성이 필요하다.  
> 
> 자신이 작성한 코드에 대해 더 심도있게 준비하여 이해도를 높여야 할 것 같다. 
