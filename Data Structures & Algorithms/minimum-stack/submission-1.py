class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.minst) > 0:
            self.minst.append(min(self.minst[-1], val))
        else: 
            self.minst.append(val)

    def pop(self) -> None:
        if len(self.st) > 0:
            self.st.pop()
        if len(self.minst) > 0:
            self.minst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
