class Solution:
    def punishmentNumber(self, n: int) -> int:
        count = 1
        map = {}
        def backtrack(number,curr_sum,square):
            nonlocal count
            nonlocal map
            if number == "":
                if curr_sum == square and square not in map:
                    map[square] = 1
                    count+= square * square
                return
            if curr_sum > square:
                return
            for i in range(len(number)):
                pick = number[:i+1]
                remaining = number[i+1:]
                curr_sum += int(pick)
                backtrack(remaining,curr_sum,square)
                curr_sum -= int(pick)
        for i in range(9,n+1):
            map = {}
            backtrack(str(i*i),0, i)       
        return count