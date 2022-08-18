def terenary_search(li,left,right,data):

    mid1 = left + (right-left)//3
    mid2 = mid1 + (right-left)//3

    if li[mid1]==data:
        return mid1+1

    if li[mid2]==data:
        return mid2+1

    if li[mid1] > data:
        return terenary_search(li,left,mid1-1,data)

    if li[mid2] < data:
        return terenary_search(li,mid1+1,right,data)

    return terenary_search(li,mid1+1,mid2-1,data)

if __name__ == '__main__':
    print("list then data\n")
    li = [int(i) for i in input().split()]
    l = 0
    r = len(li) - 1
    data = int(input())
    print(terenary_search(li,l,r,data))