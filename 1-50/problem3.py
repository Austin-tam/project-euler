#Problem 3
#O(n)

n = 600851475143

divisor = 2
answer = 0

while (n > 1):
    if (n % divisor == 0):
        n /= divisor
        if (divisor > answer):
            answer = divisor
    else:
        divisor += 1

print(answer)
