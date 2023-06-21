#python
def count_multiples(numbers):
    divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    counts = {divisor: 0 for divisor in divisors}
    
    for number in numbers:
        for divisor in divisors:
            if number % divisor == 0:
                counts[divisor] += 1
    
    return counts

# Example
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = count_multiples(numbers)
print(result)
