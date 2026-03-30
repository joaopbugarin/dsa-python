class MinStack:

    def __init__(self):
        self.stk = []
        self.min_control = []
    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_control:
            self.min_control.append(val)
            self.min = val
        else:
            self.min = min(self.min,val)
            self.min_control.append(self.min)
    def pop(self) -> None:
        self.stk.pop()
        self.min_control.pop()
        if self.min_control:
            self.min = self.min_control[-1]
    def top(self) -> int:
        return self.stk[-1]
    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.stk)
obj.push(3)
obj.push(4)
obj.push(15)
obj.push(344444)
obj.push(-33)
obj.push(42)
obj.push(-15)
obj.push(344444)
obj.push(42)
obj.push(-15)
obj.push(344444)
print(obj.stk)
obj.pop()
print(obj.stk)
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)