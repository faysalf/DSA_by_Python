def bubble_sort(L):
    n = len(L)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if (L[j] > L[j+1]):
                L[j], L[j+1] = L[j+1], L[j]

if __name__ == "__main__":
    L = [7,4,8,1,3,9,3,5,2]
    print("Before sort:",L)
    bubble_sort(L)
    print("After sort:",L)
