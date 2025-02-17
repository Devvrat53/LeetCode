'''
In-place disposition
Space: O(1) -> No ds used
Time: O(n) -> Only 1 loop used
'''
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0

        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else: 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1

if __name__ == '__main__':
    soln = Solution()
    nums = [0, 1, 0, 3, 12]
    soln.moveZeroes(nums)
    print(nums)