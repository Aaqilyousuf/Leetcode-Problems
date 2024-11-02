class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        res = []
        
        for i in range(len(code)):
            tot = 0
            for j in range(1, abs(k)+1):
                tot += code[(i+j) % len(code)] if k>0 else code[(i-j) % len(code)]
            res.append(tot) 
        return res