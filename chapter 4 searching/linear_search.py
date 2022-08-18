def linear_search(L,x):
    ln = len(L)-1       #loop a = ln dewar jonno
    i = 0
    while i <= ln:
        if L[i] == x:
            return i
        i += 1
    return -1

L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = int(input())
print(linear_search(L,x))
