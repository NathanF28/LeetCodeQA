class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        pos = [0] * n
        for i in range(n):
            pos[nums1[i]] = i

        nums3 = [pos[num] for num in nums2]

        def count_left_smaller(arr):
            res = [0] * len(arr)
            index = list(range(len(arr)))

            def merge_sort(left, right):
                if right - left <= 1:
                    return
                mid = (left + right) // 2
                merge_sort(left, mid)
                merge_sort(mid, right)

                temp = []
                i, j = left, mid
                count = 0

                while i < mid and j < right:
                    if arr[index[i]] < arr[index[j]]:
                        temp.append(index[i])
                        count += 1
                        i += 1
                    else:
                        res[index[j]] += count
                        temp.append(index[j])
                        j += 1

                while i < mid:
                    temp.append(index[i])
                    i += 1

                while j < right:
                    res[index[j]] += count
                    temp.append(index[j])
                    j += 1

                index[left:right] = temp

            merge_sort(0, len(arr))
            return res

        def count_right_greater(arr):
            res = [0] * len(arr)
            index = list(range(len(arr)))

            def merge_sort(left, right):
                if right - left <= 1:
                    return
                mid = (left + right) // 2
                merge_sort(left, mid)
                merge_sort(mid, right)

                temp = []
                i, j = mid, left
                count = 0

                while i < right and j < mid:
                    if arr[index[i]] > arr[index[j]]:
                        temp.append(index[i])
                        count += 1
                        i += 1
                    else:
                        res[index[j]] += count
                        temp.append(index[j])
                        j += 1

                while j < mid:
                    res[index[j]] += count
                    temp.append(index[j])
                    j += 1

                while i < right:
                    temp.append(index[i])
                    i += 1

                index[left:right] = temp

            merge_sort(0, len(arr))
            return res

        left_smaller = count_left_smaller(nums3)
        right_larger = count_right_greater(nums3)

        res = 0
        for j in range(n):
            res += left_smaller[j] * right_larger[j]

        return res
