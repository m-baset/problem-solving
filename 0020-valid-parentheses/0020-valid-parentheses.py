class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '{', '[']
        close = [')', '}', ']']
        if len(s) % 2 != 0:
            return False
        stack = []
        for p in s:
            if p in open:
                stack.append(p)
            elif p in close and len(stack) > 0 and open.index(stack[-1]) == close.index(p):
                stack.pop()
            else:
                return False
        return len(stack) == 0
        