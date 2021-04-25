def magic(a):
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            a[i + 1] = a[i]
            a[i] = a[i + 1]
    print(a)

magic([3, 7, 5, 1, 8])