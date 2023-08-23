class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    assert Solution().longestConsecutive(nums) == 4

    nums = [0,3,7,2,5,8,4,6,0,1]
    assert Solution().longestConsecutive(nums) == 9
