class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_sum = 1
        left_side = [1] * len(nums)
        for i in range(1, len(nums)):            
            l_sum *= nums[i-1]
            left_side[i] = l_sum
        r_sum = 1
        right_side = [1] * len(nums)
        for j in range(len(nums)-1,-1,-1):
            right_side[j] = r_sum
            r_sum *= nums[j]    
        print(left_side)   
        print(right_side) 
        for k in range(len(nums)):
            left_side[k]*=right_side[k]
        return left_side    

        