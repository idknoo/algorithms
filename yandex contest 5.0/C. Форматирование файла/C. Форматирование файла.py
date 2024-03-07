lines = int(input())
tabs = []
count = 0

for i in range(lines):
    k = int(input())
    tabs.append(k)

for i in range(lines):
    if tabs[i] % 4 == 0:
        count += tabs[i] // 4
    elif tabs[i] // 4 >= 1 and tabs[i] % 4 < 3:
        count += tabs[i] // 4 + tabs[i] % 4
    elif tabs[i] % 4 == 3:
        count += tabs[i] // 4 + 2
    else:
        count += tabs[i] % 4
print(count)
