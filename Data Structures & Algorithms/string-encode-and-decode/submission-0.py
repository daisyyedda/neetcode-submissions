class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) < 2: return []
        res = []
        idx = 0
        length = ""
        while idx < len(s):
            if '0' <= s[idx] <= '9':
                length += s[idx]
                idx += 1
            elif s[idx] == '#':
                length = int(length)
                res.append(s[idx+1:idx+length+1])
                idx = idx + length + 1
                length = ""

        return res