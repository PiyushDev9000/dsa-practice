class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_range(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        ind = -1
        n = len(nums)

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break

        if ind == -1:
            nums.reverse()
            return


        for i in range(n - 1, ind , -1):
            if nums[ind] < nums[i]:
                nums[ind], nums[i] = nums[i], nums[ind]
                break             
        
        reverse_range(nums, ind+1, n-1)