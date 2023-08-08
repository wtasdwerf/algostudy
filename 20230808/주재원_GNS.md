

<span style = "color:orange">

# 문제 제목
GNS

> 출처 : https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AV14jJh6ACYCFAYD&probBoxId=AYmbBnEa7eIDFAUe&type=PROBLEM&problemBoxTitle=HOMEWORKS&problemBoxCnt=6



## 문제

> 숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.


## 풀이

```python
   # GNS

T = int(input())

for tc in range(1, T+1):

    # N을 int 변환하고 했는데도 값이 나오지 않아서 _, N 한 이후 결과 출력
    # tc, N - 이중 #

    _, N = input().split()

    alien = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}

    alien_list = input().strip().split()

    # N의 범위에서 일치 여부를 확인하면서 해당되는 값의 value += 1

    for i in range(int(N)):
        alien[alien_list[i]] += 1

    print(f'#{tc}')

    # dict 구조에서 key 값을 찾기

    for key, value in alien.items():

        # value 다 돌면서 key 값 출력
        for _ in range(value):
            print(key, end=" ")
    print()

```
<br>

> 풀이설명

ZRO : 0, ONE : 1 대응 방식을 보고 dictionary의 key, value를 생각했습니다.
입력에 따라 각 key에 할당된 value를 더해주었고, 결산된 value들을 순회하면서 각 key 값을 출력하였습니다.


## 의문점
> 해결되지 않은 부분


<br/><br>


## 배운점
> TIL

