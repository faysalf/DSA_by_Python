def binary_search(L,x):
    left = 0
    right = len(L) - 1      #index value
    
    while left <= right:
        mid = (left + right)//2
        if L[mid] == x:
            return mid
        elif x < L[mid]:
            right = mid - 1 #if x chhuto hoy tahole right = mid-1 hobe ar left unchange thakbe
        else:
            left = mid + 1  #else left = mid+1 hobe r right unchange thakbe
    return -1
if __name__ == "__main__":
    L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    x = int(input())
    print(binary_search(L,x))
