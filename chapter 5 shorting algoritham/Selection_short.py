def selection_sort(L):
    ln = len(L)
    for i in range(0,ln-1):
        smaller = i
        for j in range(i+1,ln):
            if (L[smaller] > L[j]):     #ai if func ti sotyo hole porer if kaj korbe
                                        #cause, smaller er value change howar condition ati.
                smaller = j
        if smaller != i:        #duitir index ak na hole place change kore dite hobe
            L[i], L[smaller] = L[smaller], L[i]

if __name__ == "__main__":
    L = [4,3,2,6,7,1,9,6]
    print("Before shorting:", L)
    selection_sort(L)
    print("After shorting:", L)
