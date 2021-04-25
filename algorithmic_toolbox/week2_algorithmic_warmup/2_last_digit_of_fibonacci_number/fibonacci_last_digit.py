# Uses python3
import sys

def get_fibonacci_last_digit(n):
    last_digits = []

    last_digits.append(0)
    last_digits.append(1)

    for i in range(2, 61):
        last_digits.append((last_digits[i - 1] + last_digits[i - 2]) % 10)

    return last_digits[n % 60]



n = int(input())
print(get_fibonacci_last_digit(n))


"""def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))"""


