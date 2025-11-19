#A simple problem to understand generators
#Write a generator function called prime_numbers(limit) that yields all prime numbers up to a given limit. Then, use it to print all primes less than 50.
def prime_numbers(limit):
    for i in range(2, limit+1):
        for j in range(2, limit/2+1):
            if i%j==0:
                break
            else:
                yield i
limit = int(input("What is the limit? "))
numbers = prime_numbers(limit)
for n in numbers:
    print(n)