# import re

class Solution:
    def encode(self, strs: list[str]):
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, eStr: str):
        # test = re.split('\d\#', eStr)
        res = []
        i = 0
        while i < len(eStr):
            j = i
            while eStr[j] != '#':
                j += 1
            print(eStr[i:j])
            strLen = int(eStr[i:j])
            res.append(eStr[j + 1 : j + 1 + strLen])
            i = j + 1 + strLen
        # re.split('\d\#', eStr)
        return res 

if __name__ == "__main__":
    input = ["lint","code","love","you"]
    output = '4#lint4#code4#love3#you'
    assert Solution().encode(input) == output
    assert Solution().decode(output) == input
    assert Solution().decode(Solution().encode(input)) == input

    input = ["we", "say", ":", "yes"]
    output = '2#we3#say1#:3#yes'
    assert Solution().encode(input) == output
    assert Solution().decode(output) == input
    assert Solution().decode(Solution().encode(input)) == input

