from test_framework import generic_test


def multiply(x, y):
    # A brute force solution would be to add x repeatedly for a total of y
    # times. However, this is O(2^n), considering the case where x/y (or both)
    # are very large values, where n = bit width of x and y (If y was 2^64,
    # n = 64 here, we would have to continuously add x 2^64 times!)
    #
    # A much cleaner solution would be to understand ANY number can be
    # decomposed to the sum of powers of 2, for every set bit in that numnber.
    #
    # We know to multiply any number by a power of 2, we simply shift the number
    # to the left k times, where k is the exponent to obtain the power of 2.
    # For example:
    #
    # 2 * 7 = (00000010) * (00000111)
    #
    # Here, we would want to left shift 7 once (2^1 = 2). This would yield 14.
    #
    # With this information, we simply perform this trick for every bit set
    # within one of the operands, and add to a running sum.
    #
    # With this solution though, we'll still need to impmlement our own add().
    # This is a bit more intuitive, as we simply take the XOR of op1, op2, and
    # the ripple carry. We set the ripple carry bit when >= 2 of the 3 bits
    # are set.

    def add(a, b):
        carry_in = res = carry_out = 0
        cur_bit = 1

        # Take the same approach as mult. and right shift a and b until all
        # bits are visited. We need to reference the original a and b to
        # determine which bit index we're working with, so create temps.
        temp_a, temp_b = a, b

        while temp_a or temp_b:
            # Obtain bit for a and b
            cur_a, cur_b = (a & cur_bit), (b & cur_bit)

            res |= (cur_a ^ cur_b ^ carry_in)

            # Set ripple carry to correct value
            carry_out = (cur_a & cur_b) | (cur_a & carry_in) | (cur_b & carry_in)

            temp_a, temp_b, cur_bit = (temp_a >> 1), (temp_b >> 1), (cur_bit << 1)

            # Need to have separate carry in and out
            carry_in = carry_out << 1

        return (res | carry_in)


    res = 0

    while x:
        # Only add if bit is set
        if x & 1:
            res = add(res, y)

        # To make the check for whether the bit is set or not, we only check the
        # least significant bit. However, we'll need to right shift x every
        # iteration to make this work.
        x = (x >> 1)

        # y is by default 2^0 * k. Thus, we'll be guaranteed we're adding the
        # correct amount at every iteration if we increment k (by left shifting
        # once)
        y = (y << 1)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
