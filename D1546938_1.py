i = int(input("輸入0~15的整數："))

if 0 <= i <= 15:
    a = str(i//8%2) + str(i//4%2) + str(i//2%2) + str(i%2)
    b = str(i//8) + str(i%8)

    if i == 10:
        c = "A"
    elif i == 11:
        c = "B"
    elif i == 12:
        c = "C"
    elif i == 13:
        c = "D"
    elif i == 14:
        c = "E"
    elif i == 15:
        c = "F"
    else:
        c = str(i)

    print(a)
    print(b)
    print(c)

else:
    print("輸入錯誤")