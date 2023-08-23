class Solution:
    # linear memory and time
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output

    # not linear memory but linear time
    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] * nums[i]

        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i + 1]

        return output


if __name__ == "__main__":
    nums = [1,2,3,4]
    output = [24,12,8,6]
    assert Solution().productExceptSelf(nums) == output

    nums = [-1,1,0,-3,3]
    output = [0,0,9,0,0]
    assert Solution().productExceptSelf(nums) == output
    
    nums = [2,2,3,2]
    output = [12,12,8,12]
    assert Solution().productExceptSelf(nums) == output

