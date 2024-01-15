# n: 스위치 개수
n = int(input())
state = [-1]
input_state = list(map(int, input().split()))
state = state + input_state
students = int(input())

def on_off(i, state):
    if state[i] == 1:
        state[i] = 0
    else:
        state[i] = 1

# 남자인 경우
# 종료 조건 설정에서 문제 발생
def method_m(s_point, state):
    i = 2
    on_off(s_point, state)
    while i < len(state) // s_point:
        index = s_point * i
        on_off(index, state)
        i += 1
def method_f(s_point, state):
    on_off(s_point, state)
    head = s_point - 1
    rear = s_point + 1
    while rear < len(state):
        if state[head] != state[rear]:
            break
        else:
            on_off(head, state)
            on_off(rear, state)
            head -= 1
            rear += 1


for _ in range(students):
    gender, start_point = map(int, input().split())
    if gender == 1:
        method_m(start_point, state)

    else:
        method_f(start_point, state)

for i in range(1, len(state)):
    print(state[i], end=' ')
    if i == 20:
        print()
