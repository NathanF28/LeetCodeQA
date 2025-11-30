class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        rem = sum(nums) % p
        if not rem:
            return 0

        _min = float('inf') 
        prefix = 0
        map = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]
            curr = prefix % p

            target = (curr - rem + p) % p

            if target in map:
                _min = min(_min, i - map[target])

            #since its smallest
            map[curr] = i

        return _min if _min < len(nums) else -1
                

        