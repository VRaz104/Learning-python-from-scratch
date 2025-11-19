#A simple problem to understand generators 
##Write a generator function called prime_numbers(limit) that yields all prime numbers up to a given limit. Then, use it to print all primes less than 50.
def prime_numbers(limit):
    for i in range(2, limit + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i
limit = int(input("What is the limit? "))
numbers = prime_numbers(limit)
for n in numbers:
    print(n)