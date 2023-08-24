class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashMap = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for c in s:
            if c not in hashMap:
                stack.append(c)
            elif len(stack) > 0:
                char = stack.pop()
                if hashMap[c] != char:
                    return False
            else:
                return False
        return True if len(stack) == 0 else False
                    

if __name__ == "__main__":
    s = '()'
    assert Solution().isValid(s) is True

    s = '()[]{}'
    assert Solution().isValid(s) is True

    s = '(]'
    assert Solution().isValid(s) is False

    s = '['
    assert Solution().isValid(s) is False

    s = ']'
    assert Solution().isValid(s) is False

