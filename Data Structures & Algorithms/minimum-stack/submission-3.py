class MinStack:
    st = []
    minst = []

    def __init__(self):
        self.st = []
        self.minst = [] # keep track of current minimums

    def push(self, val: int) -> None:
        if len(self.minst) == 0:
            self.minst.append(val)
        else:
            if self.minst[-1] > val:
                self.minst.append(val)
            else:
                self.minst.append(self.minst[-1])
        self.st.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.minst.pop()
        
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
