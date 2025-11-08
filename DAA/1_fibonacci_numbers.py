import time

def fib_rec(n): 
    return n if n <= 1 else fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

n = int(input("Enter number of elements: "))

# Recursive
print("\nFibonacci (Recursive): ", end="")
start = time.time()
for i in range(n):
    print(fib_rec(i), end=" ")
end = time.time()
t_rec = (end - start) * 1e6  # microseconds

# Iterative
print("\n\nFibonacci (Iterative): ", end="")
start = time.time()
fib_iter(n)
end = time.time()
t_itr = (end - start) * 1e6

# Results
print(f"\nRecursive Time: {t_rec:.2f} µs | O(2^n) | Space: O(n)")
print(f"Iterative Time: {t_itr:.2f} µs | O(n) | Space: O(1)")
