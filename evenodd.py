# Even and Odd Counter Program

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for n in numbers:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)


# Example input
numbers = [2, 3, 4, 5, 6, 7, 9, 11, 13, 14]

count_even_odd(numbers)
# Prime Number Counter Program

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(numbers):
    prime_count = 0

    for n in numbers:
        if is_prime(n):
            prime_count += 1

    print("Prime numbers:", prime_count)


# Example input
numbers = [2, 3, 4, 5, 6, 7, 9, 11, 13, 14]

count_primes(numbers)
