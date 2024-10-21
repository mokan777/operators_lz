n = int(input())

count = 0
while n != 0:
    if n % 3 == 0:
        n -= 3
    elif n % 3 == 1:
        n -= 1
    else:  # n % 3 == 2
        n -= 2
    count += 1

print(count)