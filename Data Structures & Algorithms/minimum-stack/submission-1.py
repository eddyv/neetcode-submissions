class MinStack:
    # push(1), [1], min=1
    # push(2), [1,2], min=1
    # push(0), [1,2,0] min=0
    # Q is there a data structure we can use for min to ensure we always have the minimum element in there.
    # maybe a second stack?
    # push(1), [1], [1]
    # push(2), [1,2], peek onto minstack, pop and push new one in there. [2,1]
    # push(0), [1,2,0], [2,1,0]
    # pop(), [1,2], [2,1]
    # top(), 2
    # min(), 1

    # push(2,4,0,1,6,5)
    # [2], [2]
    # [2,4], [4,2]
    # [2,4,0], [4,2,0]
    # [2,4,0,1], [4,2,1,0]
    # [2,4,0,1,6], [4,2,1,0] <-- we don't care about 6 being added to this stack since it will always be popped before we see the other numbers!!!!

    # push (2,5,1,3,6,0,0)
    # [2], [2]
    # [2,5], [2]
    # [2,5,1], [2,1]
    # [2,5,1,3], [2,1]
    # [2,5,1,3,6], [2,1]
    # [2,5,1,3,6,0,0], [2,1,0,0]
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)

        print(f"stack: {self.stack}, minStack: {self.minStack}")


    # always called on non empty stacks
    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val == self.minStack[-1]:
            self.minStack.pop()
        print(f"stack: {self.stack}, minStack: {self.minStack}")

    # always called on non empty stacks
    def top(self) -> int:
        print(f"stack: {self.stack}, minStack: {self.minStack}")
        return self.stack[-1]
        
    def getMin(self) -> int:
        print(f"stack: {self.stack}, minStack: {self.minStack}")
        return self.minStack[-1]
