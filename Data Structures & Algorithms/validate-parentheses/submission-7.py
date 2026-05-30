class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            elif len(st) == 0:
                return False
            elif ((c == ')') and (st[-1] == '(')) or ((c == '}') and (st[-1] == '{')) or ((c == ']') and (st[-1] == '[')):
                st.pop()
            else:
                st.append(c) 

        return len(st) == 0