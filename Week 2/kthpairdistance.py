#brute force approch
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        pairArr = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = abs(nums[i] - nums[j])
                pairArr.append(diff)

        pairArr.sort()
        return pairArr[k - 1]
