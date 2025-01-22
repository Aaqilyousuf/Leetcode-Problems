class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            while stack and n < 0 < stack[-1]:
                if stack[-1] < -n:
                    stack.pop()
                elif stack[-1] == -n: # both are same so both will destroy
                    stack.pop() # here the stack top destroy
                    break # here the incoming negative asteroid is destroyed
                else:
                    break # the asteroid is smaller the the stack top so it will destroy so we didn't add it to stack
            else:
                stack.append(n)
                
        return stack