def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)    #1 return na kora porjonto ati cholbe.
                                # fact(n) ke fact(n-1) korte thakbe.
    # jokhon 1 return hobe tokhon uporer func gulu ake ake fill up kore
    # abar upore jabe. func er vitor func ke call korae recursion er kaj

if __name__=="__main__":
    inp = int(input())
    print(fact(inp))