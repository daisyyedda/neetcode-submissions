import string

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        res = 0
        for op in operations:
            if op == '+':
                score1 = st[-1]
                st.pop()
                score2 = st[-1]
                st.pop()
                st.append(score2)
                st.append(score1)
                st.append(score1+score2)
            elif op == 'D':
                st.append(2*st[-1])
            elif op == 'C':
                st.pop()
            else:
                st.append(int(op))
        res = 0
        for s in st:
            res += s
        return res