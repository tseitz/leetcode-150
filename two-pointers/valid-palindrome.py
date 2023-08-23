class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first solution is to lower, remove bad chars, reverse and compare
    
        # second is pointers
        l, r = 0, len(s) - 1
        while l < r:
            # could use another while here
            if self.alphaNum(s[r]) is False:
                r -= 1
                continue
            if self.alphaNum(s[l]) is False:
                l += 1
                continue 
            
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True


    # could write our own alphNumeric function as well
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    assert Solution().isPalindrome(s) is True

    s = "race a car"
    assert Solution().isPalindrome(s) is False

    s = " "
    assert Solution().isPalindrome(s) is True 

