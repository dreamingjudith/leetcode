from typing import List


# brute force - 7308 ms, 14.8 MB
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum += nums[j]

                if sum == target:
                    return [i, j]
                else:
                    sum -= nums[j]


# 836 ms, 15.3 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_list = [target - item for item in nums]

        for idx, item in enumerate(nums):
            if item in target_list:
                if target_list.index(item) == idx:
                    continue
                else:
                    return [idx, target_list.index(item)]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
