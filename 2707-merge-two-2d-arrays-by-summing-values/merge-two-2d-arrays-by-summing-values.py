class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums2.extend(nums1)
        map = {}
        for pair in nums2:
            if pair[0] not in map:
                map[pair[0]] = pair[1]
            else:
                map[pair[0]] += pair[1]
        return list(sorted(map.items()))


        