def selecton_sort(L):
     n = len(L)
     for i in range(0,n-1):
         shorter = i
         for j in range(i+1,n):
             if L[shorter] > L[j]:
                 shorter = j
         if shorter != i:
            L[i], L[shorter] = L[shorter], L[i]

if __name__ == "__main__":
    L = [5,8,3,2,6,9,1]
    print("Before short:", L)
    selecton_sort(L)
    print("After short:", L)
