from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq_map = Counter(s)
        liste = sorted(freq_map.items())
        
        left = ""
        middle = ""
        
        for letter, freq in liste:
            # Add half to the left side
            left += letter * (freq // 2)
            
            # If odd frequency, store ONE letter as middle
            if freq % 2 == 1:
                middle = letter
        
        # Mirror left side
        right = left[::-1]
        
        return left + middle + right
