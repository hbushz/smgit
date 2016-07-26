def fibona1(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a+b
        n = n+1
    return "Done"
