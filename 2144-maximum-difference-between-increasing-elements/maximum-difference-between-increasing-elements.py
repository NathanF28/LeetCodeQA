class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        arr = deque()
        _max = -float('inf')
        arr.append(_max)
        for i in range(len(nums)-2,-1,-1):
            _max = max(_max,nums[i+1])
            arr.appendleft(_max)
        res = -float('inf')
        for i in range(len(nums)-1):
            if nums[i] < arr[i]:
                res = max(res,arr[i]-nums[i])
        return res if res != -float('inf') else -1 