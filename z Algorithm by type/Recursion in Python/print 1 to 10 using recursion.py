def onetoten(low,high):
    if low==high:
        return low
    elif low<high:
        print(low)
        return onetoten(low+1,high)

if __name__=="__main__":
    print(onetoten(1,10))



'''def onetoten(low,high):
    if low <= high:
        print(low)
        return onetoten(low+1,high)

if __name__=="__main__":
    print(onetoten(1,10))'''