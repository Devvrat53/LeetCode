class Solution:
    def longestSubarray(self, nums):
        i, j = 0, 0
        max_window, count_zeroes = 0, 0

        while j < len(nums):
            if nums[j] == 0:
                count_zeroes += 1
            while count_zeroes > 1:
                if nums[i] == 0:
                    count_zeroes -= 1
                i += 1
            max_window = max(max_window, j - i + 1 - count_zeroes)
            j += 1
        if max_window == len(nums):
            return max_window-1
        return max_window

if __name__ == '__main__':
    soln = Solution()
    nums = [1, 1, 0, 1]
    print(soln.longestSubarray(nums))