from test_framework import generic_test


def swap_bits(x, i, j):
    if ((x >> i) & 1) != ((x >> j) & 1):
        # Don't need to swap anything if bits @ index i and j are the same.
        # Do bit mask with bit indices of i and j set, then do XOR to swap.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
