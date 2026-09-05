class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if stack:
                    if pairs[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return False if stack else True
        