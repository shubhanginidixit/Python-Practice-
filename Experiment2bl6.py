def prime_generator(n):
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num
            count += 1

        num += 1


# Dynamic input
n = int(input("Enter how many prime numbers you want: "))

for prime in prime_generator(n):
    print(prime)