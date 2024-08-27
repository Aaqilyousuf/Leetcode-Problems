class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of tuples with the value and corresponding Roman numeral
        val_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman = ""  # This will hold the final Roman numeral
        
        # Loop over the values and numerals
        for value, numeral in val_to_roman:
            # While num is larger than the value, append the numeral and subtract the value
            while num >= value:
                roman += numeral
                num -= value
        
        return roman
