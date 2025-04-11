class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            string = str(i)
            if len(string) % 2 == 1:
                continue
            mid = len(string) //2
            left = string[:mid]
            right = string[mid:]
            left_sum = 0
            right_sum = 0
            for num in left:
                left_sum += int(num)
            for num in right:
                right_sum += int(num)
            if left_sum == right_sum:
                count+=1
        return count


        