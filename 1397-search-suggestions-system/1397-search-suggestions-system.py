class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l, r = 0, len(products) - 1
        res = []
        
        for i in range(len(searchWord)):
            search = searchWord[i]
            
           
            while l <= r and (len(products[l]) <= i or products[l][i] != search):
                l += 1
            
            
            while l <= r and (len(products[r]) <= i or products[r][i] != search):
                r -= 1
            
           
            wordRemain = r - l + 1
            if wordRemain > 0:
                res.append(products[l:min(l + 3, r + 1)])
            else:
                res.append([]) 
        
        return res
