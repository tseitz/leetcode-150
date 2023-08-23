class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        # could sort hashmap and go

        # instead bucket sorting
        for c, n in counts.items():
            bucket[n].append(c)

        ans = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        return ans


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    assert Solution().topKFrequent(nums, k) == [1, 2]

    nums = [1]
    k = 1
    assert Solution().topKFrequent(nums, k) == [1]
