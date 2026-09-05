class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in s:
            stack.append(i) if i not in pairs else (stack and stack.pop() == pairs[i]) or stack.append('#')
        return not stack