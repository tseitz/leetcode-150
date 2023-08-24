class Solution:
    def findMin(self, nums: list[int]) -> int:
        ans = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                ans = min(nums[l], ans)
                break

            m = (l + r) // 2
            ans = min(nums[m], ans)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return ans

        

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    assert Solution().findMin(nums) == 1

    nums = [4,5,6,7,0,1,2]
    assert Solution().findMin(nums) == 0

    nums = [11,13,15,17]
    assert Solution().findMin(nums) == 11
