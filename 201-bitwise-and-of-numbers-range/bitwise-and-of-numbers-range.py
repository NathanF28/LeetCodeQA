class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bin_left = bin(left)[2:].zfill(32)
        bin_right = bin(right)[2:].zfill(32)
        
        # Find the common prefix
        prefix = ""
        for b1, b2 in zip(bin_left, bin_right):
            if b1 == b2:
                prefix += b1
            else:
                break
        
        # Fill the rest with '0's to complete 32-bit binary
        prefix += '0' * (32 - len(prefix))
        print(prefix) 
        # Convert back to integer
        result = int(prefix, 2)
        return result 
            