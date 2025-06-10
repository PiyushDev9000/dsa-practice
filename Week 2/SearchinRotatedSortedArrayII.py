class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if not nums:
            return False

        firstEle = 0
        lastEle = len(nums) - 1

        while firstEle <= lastEle:
            mid = (firstEle + lastEle) // 2

            # ✅ Case 1: Found target
            if nums[mid] == target:
                return True

            # 🔁 Handle duplicates: shrink range
            if nums[firstEle] == nums[mid] == nums[lastEle]:
                firstEle += 1
                lastEle -= 1

            # ✅ Left half is sorted
            elif nums[firstEle] <= nums[mid]:
                if nums[firstEle] <= target < nums[mid]:
                    lastEle = mid - 1
                else:
                    firstEle = mid + 1

            # ✅ Right half is sorted
            else:
                if nums[mid] < target <= nums[lastEle]:
                    firstEle = mid + 1
                else:
                    lastEle = mid - 1

        # ❌ If we exit the loop, target was not found
        return False
