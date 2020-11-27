num_set = [0]*9

room = input()
for i in range(len(room)):
    if room[i] == '9':
        num_set[6] += 1
    else:
        num_set[int(room[i])] += 1
if num_set[6]%2 == 1:
    num_set[6] //= 2
    num_set[6] += 1
else:
    num_set[6] //= 2

print(max(num_set))
