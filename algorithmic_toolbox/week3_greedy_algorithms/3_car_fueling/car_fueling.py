# python3
import sys


def compute_min_refills(distance, tank, stops):
    current_refill = 0
    last_refill = 0
    total_refills = 0
    stops.append(distance)
    stops.insert(0, 0)

    if tank >= distance:
        return 0

    while current_refill < len(stops) - 1:
        last_refill = current_refill

        while (current_refill < len(stops) - 1) and ((stops[current_refill + 1] - stops[last_refill]) <= tank):
            current_refill += 1

        if current_refill == last_refill:
            return -1
        
        if current_refill < len(stops) - 1:
            total_refills += 1

    return total_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
