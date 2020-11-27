num = int(input("Enter a number: "))

if num == 0:
    print("0 영(zero)")
elif num == 999:
    print("999 Bye 종료합니다!!")
elif num<0:
    if num%2 == 0:
        print("{} 음수, 짝수".format(num))
    else:
        print("{} 음수, 홀수".format(num))
elif num > 0:
    if num%2 == 0:
        print("{} 양수, 짝수".format(num))
    else:
        print("{} 양수, 홀수".format(num))
