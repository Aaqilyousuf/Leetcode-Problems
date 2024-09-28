class BrowserHistory:

    def __init__(self, homepage: str):
        self.st1 = [homepage]
        self.st2 = []
    def visit(self, url: str) -> None:
        self.st1.append(url)
        self.st2.clear()
    def back(self, steps: int) -> str:
        while steps > 0 and len(self.st1) > 1:
            self.st2.append(self.st1.pop())
            steps-=1
        return self.st1[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.st2:
            self.st1.append(self.st2.pop())
            steps -= 1
        return self.st1[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)