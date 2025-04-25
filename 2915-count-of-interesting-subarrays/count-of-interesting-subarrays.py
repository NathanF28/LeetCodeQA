class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        isInteresting = [-1] * len(nums)
        prefix = 0
        map = defaultdict(int)
        map[0] = 1
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                prefix+=1
            isInteresting[i] = prefix % modulo
        res = 0
        for pref in isInteresting:
            need = (pref - k + modulo) % modulo
            res+= map[need]
            map[pref]+=1
        return res
            
