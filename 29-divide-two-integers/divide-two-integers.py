
class Solution(object):
    def divide(self, dividend, divisor):

        # Handle the overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Determine the sign of the answer
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Keep subtracting the largest possible multiple
        while dividend >= divisor:

            value = divisor
            multiple = 1

            while dividend >= (value << 1):
                value = value << 1
                multiple = multiple << 1

            dividend -= value
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        return quotient
