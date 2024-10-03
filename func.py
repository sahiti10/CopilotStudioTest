# Problem 1: Simple Addition
def add_numbers(a, b):
    return a + b

# Problem 2: Sorting a List
def sort_list(arr):
    return sorted(arr)

# Problem 3: Fibonacci Sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

# Problem 4: Checking Prime Numbers
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Problem 5: Finding Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Problem 6: String Reversal
def reverse_string(s):
    return s[::-1]

# Problem 7: Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# Problem 8: Find Maximum in List
def find_max(arr):
    return max(arr)

# Problem 9: Sum of Digits
def sum_of_digits(n):
    return sum([int(digit) for digit in str(n)])

# Problem 10: Greatest Common Divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test cases for each problem
if __name__ == "__main__":
    # Testing Addition
    print("Addition of 3 and 5:", add_numbers(3, 5))
    
    # Testing Sorting
    print("Sorted list:", sort_list([5, 3, 8, 1, 2]))
    
    # Testing Fibonacci Sequence
    print("Fibonacci sequence of 7 terms:", fibonacci(7))
    
    # Testing Prime Checking
    print("Is 11 prime?:", is_prime(11))
    
    # Testing Factorial
    print("Factorial of 5:", factorial(5))
    
    # Testing String Reversal
    print("Reversed string of 'hello':", reverse_string("hello"))
    
    # Testing Palindrome Check
    print("Is 'racecar' a palindrome?:", is_palindrome("racecar"))
    
    # Testing Find Maximum in List
    print("Maximum value in [1, 9, 3, 7, 5]:", find_max([1, 9, 3, 7, 5]))
    
    # Testing Sum of Digits
    print("Sum of digits of 12345:", sum_of_digits(12345))
    
    # Testing GCD
    print("GCD of 48 and 18:", gcd(48, 18))
