class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def search(rem, turn, score1,score2):
            if not rem:
                return score1 >= score2

            c1 = search(
                rem[1:], 
                0 if turn else 1,
                score1 + rem[0] if turn == 1 else score1,
                score2+ rem[0] if not turn else score2)
            c2 = search(
                rem[:-1], 
                0 if turn else 1,
                score1 + rem[-1] if turn == 1 else score1,
                score2+ rem[-1] if not turn else score2)
            
            if turn:
                return c1 or c2
            else:
                return c2 and c1
        return search(nums,1,0,0)
