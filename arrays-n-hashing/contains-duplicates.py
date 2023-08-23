class Solution:
    @staticmethod
    def containsDuplicate(nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


def test_contains_duplicates():
    nums = [1,2,3,1]
    assert Solution.containsDuplicate(nums) is True 

    nums = [1,2,3,4]
    assert Solution.containsDuplicate(nums) is False

    nums = [1,1,1,3,3,4,3,2,4,2]
    assert Solution.containsDuplicate(nums) is True 


if __name__ == "__main__":
    test_contains_duplicates()
