class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            value = target - v
            if value in hashmap:
                return [hashmap.get(value),i]
            hashmap[v] = i