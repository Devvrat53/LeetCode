class Solution:
    def productExceptSelf(self, nums):
        product_lst = [1] * len(nums)

        for i in range(1, len(nums)):
            product_lst[i] = product_lst[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            product_lst[i] *= right
            right *= nums[i]
        
        return product_lst

if __name__ == '__main__':
    soln = Solution()
    nums = [1, 2, 3, 4]
    print(soln.productExceptSelf(nums))