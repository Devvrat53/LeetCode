class Solution:
    def longestOnes(self, nums, k):
        i, j = 0, 0
        max_window, num_zeroes = 0, 0

        while j < len(nums):
            if nums[j] == 0:
                num_zeroes += 1
            while num_zeroes > k:
                if nums[i] == 0:
                    num_zeroes -= 1
                i += 1
            max_window = max(max_window, j-i+1)
            j += 1
        return max_window

if __name__ == '__main__':
    soln = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(soln.longestOnes(nums, k))