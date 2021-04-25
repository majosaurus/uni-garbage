# Uses python3
import sys

def get_change(m):
	coins_total = 0
	coins = [10, 5, 1]

	if m <= 0:
		return 0

	for i in range(len(coins)):
		if coins[i] <= m:
			amount = m // coins[i]
			coins_total += amount
			m = m - (amount * coins[i])

	return coins_total

if __name__ == '__main__':
	m = int(sys.stdin.readline())
	print(get_change(m))