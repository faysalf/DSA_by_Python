def insurtion_sort(li):
    ln = len(li)
    for i in range(1,ln):
        j = i
        sorter = li[i]
        while (j>0) and (li[j-1] > li[j]):
            li[j],li[j-1] = li[j-1], li[j]
            j -= 1
    return li

if __name__ == "__main__":
    li = list(map(int,input().split()))
    print(insurtion_sort(li))
