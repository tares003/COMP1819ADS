n = int(input())

is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n/2)):
        if n % i == 0:
            is_prime = False
            break
        else:
            is_prime = True

print(is_prime)
