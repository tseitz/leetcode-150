class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # my solution
        # for i in range(length):
        #     n = nums[i]
        #     lookingFor = target - n
        #     j = i + 1
        #     for j in range(length - j):
        #         if lookingFor == nums[j]:
        #             return True
        # return False

        # hash map solution
        prevHash = {}
        for i, n in enumerate(nums):
            lookingFor = target - n
            if lookingFor in prevHash:
                return [prevHash[lookingFor], i]
            prevHash[n] = i
        return [0, 0]


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    assert Solution().twoSum(nums, target) == [0, 1]
    
    nums = [3,2,4]
    target = 6
    assert Solution().twoSum(nums, target) == [1, 2]

    nums = [3,3]
    target = 6
    assert Solution().twoSum(nums, target) == [0, 1]
