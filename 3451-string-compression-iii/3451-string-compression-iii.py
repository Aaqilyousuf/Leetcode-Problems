class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        
        comp = []
        count = 1
        
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
                # If count reaches 9, append "9" + character to comp, then reset count
                if count > 9:
                    comp.append(f"9{word[i - 1]}")
                    count = 1
            else:
                # Append count and character to comp
                comp.append(f"{count}{word[i - 1]}")
                count = 1  # Reset count for new character
        
        # Append the final character group
        comp.append(f"{count}{word[-1]}")
        
        return "".join(comp)