def get_fibonacci_last_digit(n):
    last_digits = []

    last_digits.append(0)
    last_digits.append(1)

    for i in range(2, 61):
        last_digits.append((last_digits[i - 1] + last_digits[i - 2]) % 10)

    print(last_digits)

n = int(input())
print(get_fibonacci_last_digit(n))