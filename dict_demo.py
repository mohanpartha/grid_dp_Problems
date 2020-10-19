def readdata(indv):
    indv_disc = {}
    for i in range(indv):
        k = [(e.strip()) for e in input().split()]
        indv_disc[k[1]+k[2]] = k[0]
    return indv_disc

def querydata(datadict, key):
    testq=[]
    for ti in range(nos[1]):
        q = [int(e.strip()) for e in input().split()]
        listToStr = ''.join(map(str, q))
        testq.append(listToStr)
    for m in range(len(testq)):
        print(datadict.get(testq[m],-1))

if  __name__ == "__main__":
    tests = int(input().strip())

    for z in range(tests):
        nos = [int(e.strip()) for e in input().split()]
        datadict = readdata(nos[0])
        querydata(datadict, nos[1])
        print()