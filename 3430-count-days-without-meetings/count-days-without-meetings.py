class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meet= sorted(meetings)
        count = meet[0][0] - 1
        end = meet[0][1]
        print(meet)
        for pair in meet[1:]:
            if pair[0] > end:
                count+= pair[0] - end - 1
                print(pair)
            end = max(pair[1],end)
        count+= days-end
        return count
                


                

        