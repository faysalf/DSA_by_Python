def insurtion_sort(L):
    n = len(L)
    for i in range(1,n):
        sorter = L[i]
        while (L[i-1] > sorter) and (i > 0): #i>0 hole i-1 possible.tai i>0
            L[i], L[i-1] = L[i-1], L[i]
            i -= 1

if __name__ == "__main__":
    L = [3,2,5,3,7,9,3,9,5,1]
    print("Befor sort:",L)
    insurtion_sort(L)
    print("After sort:",L)
