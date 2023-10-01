t = int(input())
for j in range (t):
    a, b, c = input()
    d, e, f = input()
    g, h, i = input()
    
    if a == d == g!= "." or a == e == i!= "." or a == b == c != ".":
        print(a)
    elif b == e == h!= "." or d == e == f!= "." or c == e == g != ".":
        print(e)
    elif c == f == i!= "." or g == h == i != ".":
        print(i)
    else:
        print("DRAW")
