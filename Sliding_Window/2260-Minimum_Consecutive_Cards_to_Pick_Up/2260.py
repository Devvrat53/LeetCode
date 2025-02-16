from math import inf

class Solution:
    def minimumCardPickup(self, cards): 
        if len(cards) <= 1:
            return -1
        i, j = 0, 0
        element_present = set()
        max_length = inf

        while j < len(cards):
            while cards[j] in element_present:
                if (j-i+1) < max_length:
                    max_length = j-i+1
                element_present.remove(cards[i])
                i += 1
            element_present.add(cards[j])
            j += 1

        if max_length != inf:
            return max_length
        else:
            return -1
        
if __name__ == '__main__':
    cards = [3, 4, 2, 3, 4, 7]
    soln = Solution()
    print(soln.minimumCardPickup(cards))