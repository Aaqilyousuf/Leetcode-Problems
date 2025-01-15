class Solution:
    def minimizeXor(self, num1, num2):
        
        set_bits_num2 = bin(num2).count('1')

        # Start with num1 and try to adjust bits to match set_bits_num2
        result = 0
        for i in range(31, -1, -1):  # Iterate through all 32 bits
            if set_bits_num2 == 0:  # If we've matched all set bits
                break
            if num1 & (1 << i):  # If the bit in num1 is set
                result |= (1 << i)  # Set the same bit in result
                set_bits_num2 -= 1  # Decrease the count of required set bits

        # If there are still more set bits needed, add them from the lowest bits
        for i in range(32):
            if set_bits_num2 == 0:
                break
            if not (result & (1 << i)):  # If the bit is not already set
                result |= (1 << i)  # Set the bit in result
                set_bits_num2 -= 1

        return result
