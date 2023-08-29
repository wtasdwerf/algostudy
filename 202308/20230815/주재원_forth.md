<br/><Br>

<span style = "color:orange">

# 문제 제목
Forth

> 출처 : https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AYZSTZWqrz4DFARc&probBoxId=AYmbBU3a7c0DFAUe&type=USER&problemBoxTitle=PRACTICE&problemBoxCnt=27


<br/><br>

## 문제

> 문제설명

숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.

 

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

## 풀이

```python
   T = int(input())
for tc in range(1, T + 1):

    arr = list(input().split())
    
    # 연산자 리스트
    oper = '+-/*'
    stack = []
    
    # i = . , 연산자, 숫자일 때의 case

    for i in arr:
        if i == '.':
            # stack 길이에 따른 pop 또는 error 출력
            # stack == 1인 경우에만 숫자 꺼내기 가능
            if len(stack) == 1:
                print(f'#{tc} {stack.pop()}')
            else:
                print(f'#{tc} error')
            break

        elif i in oper:
            if len(stack) < 2:
                print(f'#{tc} error')
                break

            # pop 순서에 따라서 값 두 개의 순서 유의
            b = stack.pop()
            a = stack.pop()

            if i == '+':
                stack.append(a + b)

            elif i == '-':
                stack.append(a - b)

            elif i == '*':
                stack.append(a * b)

            else:
                stack.append(a // b)
                
        # 숫자인 경우 정수 형태로 변환
        else:
            stack.append(int(i))

```
<br>

> 풀이설명

리스트 내의 요소를 크게 세 가지로 나누고 '.'인 경우에는 스택의 숫자를 꺼내는 기능을 하는 stack.pop()
'.', 연산자인 사례에서 stack의 길이에 따라 조건을 나누는 부분은 생각보다 쉽지 않았습니다.


## 의문점
> 해결되지 않은 부분


<br/><br>


## 배운점
> TIL

