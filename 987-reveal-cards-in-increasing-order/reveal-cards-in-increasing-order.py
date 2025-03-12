class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)[::-1]
        q = deque()
        for card in deck:
            if q:
                q.appendleft(q.pop())
            q.appendleft(card)
        return list(q) 