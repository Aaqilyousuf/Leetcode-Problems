from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  
        path = []  
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]  
        
        def backtrack(start: int):
            if start == len(s):  
                res.append(path[:])  
                return
            
            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):  
                    path.append(s[start:end+1])  
                    backtrack(end + 1)  
                    path.pop()  
                
        backtrack(0)
        return res
