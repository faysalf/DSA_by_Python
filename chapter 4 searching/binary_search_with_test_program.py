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
    
    for x in range(1,22):               #upto 21. 1ti beshi print kora hoyese ja list a nei bujhanor jonno.akkhetre -1 kaj korbe
        position = binary_search(L,x)
        if position == -1:              #list a element ti na pawa gele
            if x in li:
                print(x,"is in L but function returned -1")
            else:
                print(x,"is not in L")
        else:
            if L[position] == x:
                print(x,"found is correct position.")
            else:
                print("binary search returned",position,"for",x,"which is incorrect")
    print("programm terminated")

        
    print(binary_search(L,x))
