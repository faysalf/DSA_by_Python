def merge_sort(L):
    size = len(L)
    if size>1:
        mid = size//2
        left_arr = L[:mid]
        left_len = len(left_arr)
        right_arr = L[mid:]
        right_len = len(right_arr)

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0
        while i<left_len and j<right_len:
            if left_arr[i]<right_arr[j]:
                L[k] = left_arr[i]
                i += 1
            elif left_arr[i]>right_arr[j]:
                L[k] = right_arr[j]
                j += 1
            k += 1

        while i<left_len:
            L[k] = left_arr[i]
            i += 1
            k += 1
        while j<right_len:
            L[k] = right_arr[j]
            j += 1
            k += 1
    return L

if __name__=="__main__":
    L = [5,33,6,23,96,2]
    print(merge_sort(L))