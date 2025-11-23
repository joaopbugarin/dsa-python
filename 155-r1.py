class MinStack:
    def __init__(self):
        self.stk = []
        self.min_stk = []
    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
            self.min = val
        else:
            self.min = min(val, self.min)
            self.min_stk.append(self.min)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        if self.min_stk:
            self.min = self.min_stk[-1]

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        if self.min_stk:
            return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(-4)
obj.push(0)
obj.push(3)
obj.push(38)
obj.push(0)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
