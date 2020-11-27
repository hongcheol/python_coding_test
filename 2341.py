def solution(n, weak, dist):
    answer = 0
    dist.sort(reverse = True)
    ans = []
    print(dist)
    for i in range(len(weak)):
        array = weak[i:]
        for j in range(i):
            array.append(weak[j]+n)
        print(array)
        l = 0
        count = 0
        for case in dist:
            l += case
            count += 1
            if array[-1] - array[0] <= l:
                ans.append(count)
                break
    print(ans)
    if ans:
        answer = min(ans)
        return answer
    return -1

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
ans = solution(n,weak,dist)
print(ans)
