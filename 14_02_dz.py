def outer(a, b, c):
    def inner(i, j):
        return i * j

    global s
    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


outer(2, 4, 6)
print(s)

outer(5, 8, 2)
print(s)
outer(1, 6, 8)
print(s)