def merge_sort(L):
    #duita list a divide korbo
    size = len(L)
    if size>1:
        mid = size//2
        left_list = L[:mid]
        left_len = len(left_list)
        right_list = L[mid:]
        right_len = len(right_list)

        merge_sort(left_list)       #merge upto 2 element
        merge_sort(right_list)
        #duiti list er elementguluke compare kore L list a insert korbo. ate kono impect porbena.
        #cause agee left & right list a devide kore alada kore rekhechhi.

        i = j = k = 0
        while i<left_len and j<right_len:
            if left_list[i]<right_list[j]:
                L[k] = left_list[i]
                i += 1
            else:
                L[k] = right_list[j]
                j += 1
            k += 1

        while i<left_len:     #merge er baire thaka elementgulu L a insert korbe
            L[k] = left_list[i]
            i += 1
            k += 1
        while j<right_len:
            L[k] = right_list[j]
            j += 1
            k += 1
    return L

if __name__ == "__main__":
    L = [5, 1, 3, 2, 4,53,23,4,223,4,5]
    result = merge_sort(L)
    print(result)