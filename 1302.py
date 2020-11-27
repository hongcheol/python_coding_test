n = int(input())
d = {}

for _ in range(n):
    book = input()
    if book not in d:
        d[book] = 1
    else:
        d[book] += 1

target = max(d.values())
array = []

for book, number in d.items():
    if number == target:
        array.append(book)
print(sorted(array)[0])
