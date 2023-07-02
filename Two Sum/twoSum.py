class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]
        return None

test = [2, 7, 11, 15]
target = 9

solution = Solution()
print(solution.twoSum(test, target))
    