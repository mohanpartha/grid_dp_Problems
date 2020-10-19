def modprd(a):
    mod = 10**9 + 7
    return (a%mod)

def modsum(a,b):
    mod = 10**9 + 7
    return (a%mod +b%mod)%mod

def ncr(n,i,dict):
    if n==i or i==0:
        return modsum(1,0)
    else:
        return modsum(ncr(n-1,i,dict), ncr(n-1,i-1,dict) )
def solve(n,dict):
    arr = []
    for i in range(n+1):
        dict[n,i] = ncr(n,i,dict)

    for i in range(n+1):
        arr.append(dict.get((n,i)))
    return arr

if  __name__ == "__main__":
    import sys
    import os
    # print(sys.getrecursionlimit())
    sys.setrecursionlimit(10000)
    tests = int(input().strip())
    dict = {}
    for z in range(tests):
        p = int(input().strip())
        ncrof = solve(p,dict)
        print(' '.join(map(str,ncrof)))
