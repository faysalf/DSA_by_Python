def selection_sort(li):
    #li = [4,2,5,3,4]
    ln = len(li)
    for i in range(0,ln-1):
        index_min = i
        
        for j in range(i+1,ln):
            if li[index_min] > li[j]:
                index_min = j

        if index_min != i:
            li[index_min], li[i] = li[i], li[index_min]
    print(li)

if __name__ == "__main__":
    li = list(map(int,input().split()))
    selection_sort(li)
