def calculate_prime_numbers(n):
    # Simulate a CPU-intensive task (calculating prime numbers)
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    print("Starting the long-running build process...")
    
    # Simulate a CPU-intensive task that takes time
    prime_numbers = calculate_prime_numbers(10000)
    
    print("Build process completed!")
