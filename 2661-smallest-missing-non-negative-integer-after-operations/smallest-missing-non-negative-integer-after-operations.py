class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        map = defaultdict(int)
        for num in nums:
            val = num % value
            map[val]+=1
        print(map)
        for i in range(len(nums)):
            check = i % value
            if check not in map:
                return i
            if map[check] >= 1:
                map[check]-=1
                if map[check] == 0:
                    del map[check]
        return len(nums)