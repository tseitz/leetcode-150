from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            # this will be the key
            group = [0] * 26

            # count each char
            for c in s:
                group[ord(c) - ord('a')] += 1
        

            res[tuple(group)].append(s)
    
        return list(res.values())


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    solution = Solution().groupAnagrams(strs)
    assert Solution().groupAnagrams(strs) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    strs = [""]
    assert Solution().groupAnagrams(strs) == [[""]]

    strs = ["a"]
    assert Solution().groupAnagrams(strs) == [["a"]]
