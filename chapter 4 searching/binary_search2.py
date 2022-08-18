def binary_search(L,n):
    left = 0
    right = len(L) - 1
    while (left <= right):
        mid = (left + right)//2
        if (n == L[mid]):
            return mid
        elif (n < L[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return -1
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
n = int(input())
print(binary_search(L,n))
