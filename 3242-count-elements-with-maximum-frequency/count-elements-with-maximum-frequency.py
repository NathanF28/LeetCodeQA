class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0] * 101
        maxFreq = 0
        for num in nums:
            freq[num] += 1
            maxFreq = max(maxFreq, freq[num])
        
        ans = 0
        for f in freq:
            if f == maxFreq:
                ans += maxFreq
        return ans
        