def negative_numbers(n):  # n = []
    if not n:
        return 0
    count = 0  # 0
    if n[0] < 0:
        count += 1
    return negative_numbers(n[1:]) + count  # 1 + 0 + 0 + 1 + 1 + 0 + 0


lst = [-2, 3, 8, -11, -4, 6]
print(negative_numbers(lst))