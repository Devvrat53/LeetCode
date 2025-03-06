class Solution:
    def largestAltitude(self, gain):
        if len(gain) == 1:
            if gain[0] < 0:
                return 0
            return gain[0]

        prefix_sum = [0] * (len(gain)+ 1)
        highest = prefix_sum[0]

        for i in range(1, len(gain)+1):
            prefix_sum[i] = prefix_sum[i-1] + gain[i-1]
            #print(prefix_sum[i])
            if highest < prefix_sum[i]:
                highest = prefix_sum[i]
        return highest

if __name__ == '__main__':
    soln = Solution()
    gain = [-5,1,5,0,-7]
    print("Highest altitude: ", soln.largestAltitude(gain))