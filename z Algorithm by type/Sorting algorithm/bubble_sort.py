def bubble_sort(li):
    #li = [5,3,6,2,89,7]
    ln = len(li)
    for i in range(0,ln-1):
        for j in range(i+1,ln):
            if li[i] > li[j]:
                li[i],li[j] = li[j], li[i]
    return li

if __name__=="__main__":
    li =  list(map(int,input().split()))
    print(bubble_sort(li))
