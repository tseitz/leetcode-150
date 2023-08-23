class Solution:
    def maxArea(self, heights: list[int]) -> int:
        res = 0
        
        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    answer = 49
    assert Solution().maxArea(height) == answer

    height = [1,1]
    answer = 1
    assert Solution().maxArea(height) == answer
