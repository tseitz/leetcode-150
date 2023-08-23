class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # my first attempt, i realize this section is called 2 pointers -_-
        # output = []
        # nums.sort()
        # i = 0
        # j = 1
        # k = 2
        # while i < len(nums) - 2:
        #     while j < len(nums) - 1 and (nums[i] == 0 or nums[i] != nums[i - 1]):
        #         while k < len(nums): 
        #             sum = nums[i] + nums[j] + nums[k]
        #             if sum == 0:
        #                 output.append([nums[i], nums[j], nums[k]])
        #             k += 1
        #         j += 1
        #         k = j + 1
        #     i += 1
        #     j = i + 1
        #     k = j + 1
        # return output
        
        # better to do 2 pointers, l and r 
        output = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return output


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    answer = [[-1,-1,2],[-1,0,1]]
    assert Solution().threeSum(nums) == answer

    nums = [0,1,1]
    answer = []
    assert Solution().threeSum(nums) == answer

    nums = [0,0,0]
    answer = [[0,0,0]]
    assert Solution().threeSum(nums) == answer
