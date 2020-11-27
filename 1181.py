word_len = [[] for _ in range(51)]

n = int(input())

for _ in range(n):
    string = input()
    if string not in word_len[len(string)]:
        word_len[len(string)].append(string)

for words in word_len:
    if words == []:
        continue
    else:
        words.sort()
        for word in words:
            print(word)
