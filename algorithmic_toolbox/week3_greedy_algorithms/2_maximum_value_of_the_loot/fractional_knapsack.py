# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0000
    ratio = []
    
    for i in range(len(weights)):
        ratio.append(values[i]/weights[i])
    print(ratio)

    
    

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
