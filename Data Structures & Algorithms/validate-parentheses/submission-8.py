class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            elif len(st) == 0:
                return False
            elif (st[-1]== '(' and c == ')') or (st[-1] == '[' and c == ']') or (st[-1] == '{' and c == '}'):
                st.pop()
            else:
                st.append(c)
        return len(st) == 0