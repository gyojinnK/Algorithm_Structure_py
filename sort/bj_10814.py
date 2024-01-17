n = int(input())
members = []

for i in range(n):
    age, name = map(str, input().split())
    members.append((int(age), i, name))

members.sort()
for i in range(n):
    age, idx, name = members[i]
    print(age, name)