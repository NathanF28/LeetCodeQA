from collections import defaultdict
from heapq import heapify,heappop,heappush,heappushpop
class FoodRatings:

    def __init__(self,foods, cuisines, ratings):
        self.cuisineMap = defaultdict(list)
        self.ratingMap = defaultdict(int)
        self.foodMap = defaultdict(str)
        for i in range(len(foods)):
            cuisine = cuisines[i]
            food = foods[i]
            rating = ratings[i]
            heappush(self.cuisineMap[cuisine], (-rating, food))
            self.ratingMap[food] = rating
            self.foodMap[food] = cuisine

    def changeRating(self, food, newRating):
        self.ratingMap[food] = newRating
        cuisine = self.foodMap[food]
        heappush(self.cuisineMap[cuisine], (-newRating,food))

    def highestRated(self,cuisine):

        while self.cuisineMap[cuisine]:
            rating, candidateFood = self.cuisineMap[cuisine][0]
            if self.ratingMap[candidateFood] != -rating:
                heappop(self.cuisineMap[cuisine])
                continue
            return candidateFood

