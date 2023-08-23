class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # kinda cheating
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)  # sort it and return if same
        
        # could create hashmap
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
        


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    assert Solution().isAnagram(s, t) is True

    s, t = "rat", "car"
    assert Solution().isAnagram(s, t) is False
