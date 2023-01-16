class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)):
            if len(s) % i != 0:
                continue
            sub = s[:i]
            exist = False
            j = 1
            while (j*i + i) <= len(s):
                if s[i*j:i*j+i] == sub:
                    exist = True
                else:
                    exist = False
                    break
                j += 1
            if exist:
                return True
        return False