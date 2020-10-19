def modsum(a):
    mod = 10**9 + 7
    return (a%mod)

def calccount(n,k,dict):
    print(n,k)
    sum=0
    if (n,k) in dict:
        return dict.get((n,k))

    if (n==0 ):
        dict[(n,k)] = 0
        return 0
    
    if (k==0):
        dict[(n,k)] = 1
        return 1
    else:
        lim = min(k, n-1)
        print('min ',lim)
        for i in range(lim):
            print('n,k,i',n,k,i)
            sum += calccount(n-1, k-i, dict)
            print('sum', sum)
    
    print(dict)
    dict[(n,k)] = modsum(sum)
    return sum

if  __name__ == "__main__":
    import sys
    # print(sys.getrecursionlimit())
    sys.setrecursionlimit(10000)
    tests = int(input().strip())
    dict = {}
    for z in range(tests):
        p = int(input().strip())
        calcc = calccount(p,dict)
        print(calcc)
