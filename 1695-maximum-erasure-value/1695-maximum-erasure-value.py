class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        _max = 0
        l = 0
        _sum = 0
        check = defaultdict(int)
        for r in range(len(nums)):
            while l < len(nums) and nums[r] in check:
                check[nums[l]]-=1
                if check[nums[l]] == 0:
                    del check[nums[l]]
                _sum-= nums[l]
                l+=1
            check[nums[r]]+=1
            _sum+= nums[r]
            _max = max(_sum,_max)
        return _max