def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

# Specify the range
start_range = 1
end_range = 100

print_primes(start_range, end_range)
