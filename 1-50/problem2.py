#Problem 2
#O(n)

fibDict = {0: 1, 1: 1}
answer = 0

def fib(x):
    if (x <= 1):
        return 1
    elif x in fibDict:
        return fibDict[x]
    else:
        global answer
        fibDict[x] = fib(x - 1) + fib(x - 2)
        if (fibDict[x] <= 4000000 and fibDict[x] % 2 == 0):
            answer += fibDict[x]
        return fibDict[x]

fib(100)
print(answer)
