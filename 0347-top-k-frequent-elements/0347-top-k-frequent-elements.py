class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums).most_common(k)

        res = []
        for first,second in count:
            res.append(first)
        return res
