from test_framework import generic_test


def parity(x):
    # Parity behavior is naturally implemented by XOR. While a brute force
    # solution would involve visiting every bit in x and flipping the
    # parity bit, this solution can be improved by realizing taking the XOR
    # of the first and seond half of x will yield in a value which contains
    # the correct parity. If we cache the value in the bits half of lower
    # significance, we can repeatedly do this XOR with the two halves until
    # the final parity value is stored in the lowest significant bit.
    # This would improve runtime from O(n) to O(log(n)), where
    # n = bit width of x.
    x ^= (x >> 32)
    x ^= (x >> 16)
    x ^= (x >> 8)
    x ^= (x >> 4)
    x ^= (x >> 2)
    x ^= (x >> 1)

    return (x & 1)


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
