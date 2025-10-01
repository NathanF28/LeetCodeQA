class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        

        count = numBottles
        while numBottles >= numExchange:
            rem = numBottles % numExchange
            bot = numBottles // numExchange
            count += bot
            numBottles  = rem + bot
        return count