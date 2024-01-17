n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

for i in range(len(lst)):
    print(lst.pop())