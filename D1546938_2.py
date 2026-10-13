A = int(input())
B = int(input())

if A != 0 and A != 1 or B != 0 and B != 1:
    print("輸入錯誤")
else:
    if A == 1 or B == 1:
        OR = 1
    else:
        OR = 0
    if A == 1 and B == 1:
        AND = 1
    else:
        AㄎND = 0
    if A != B:
        XOR = 1
    else:
        XOR = 0

    print(f"OR={OR}")
    print(f"AND={AND}")
    print(f"XOR={XOR}")