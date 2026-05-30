class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in "([{":
                st.append(c)
            else:
                if not st or st[-1] != pairs[c]:
                    return False
                st.pop()

        return len(st) == 0
