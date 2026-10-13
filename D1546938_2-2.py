A = int(input())
B = int(input())
S = int(input())

if A not in (0, 1) or B not in (0, 1) or S not in (0, 1):
    print("輸入錯誤")
else:
    if A ^ B:
        middle = 1
    else:
        middle = 0

    if middle and S:
        start = 1
    else:
        start = 0

    print(f"第一個閘輸出={middle}")
    print(f"允許啟動={start}")