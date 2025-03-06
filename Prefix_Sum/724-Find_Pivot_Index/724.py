class Solution:
    def pivotIndex(self, nums):
        leftSum = 0
        totalSum = sum(nums)

        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum: 
                return i
            leftSum += nums[i]
        return -1
    
if __name__ == '__main__':
    soln = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(soln.pivotIndex(nums))