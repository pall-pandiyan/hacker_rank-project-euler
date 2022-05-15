# Enter your code here. Read input from STDIN. Print output to STDOUT

factorials = [0]*10

def f(n):
    sum = 0
    s = str(n)
    for ch in s:
        sum += factorials[int(ch)]
    return sum

def sf(n):
    fn = f(n)
    if fn<10:
        return fn
    sum = 0
    s = str(fn)
    for ch in s:
        sum += int(ch)
    return sum

def g(i):
    target = i
    i = 1
    while(sf(i) != target):
        i += 1 
    print("g(",i,") is:",target)
    return i
    
def sg(i):
    gi = g(i)
    if gi<10:
        return gi
    sum = 0
    s = str(gi)
    for ch in s:
        sum += int(ch)
    return sum

def main():
    factorials[1] = 1
    for i in range(2,10):
        factorials[i] = factorials[i-1] * i        

    # query = int(input().strip())
    # for i in range(query):
    #     [n,m] = list(map(int,input().strip().split()))
    #     print(sg(n)%m)

    n=3
    print("sg(",n,"):")
    result = 0
    for i in range(n,0,-1):
        result += sg(i)
    print("result is:", result)
    
if __name__=="__main__":
    main()
