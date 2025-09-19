class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        possible = []
        map = {}

        def choose(_sum, path):

            if _sum == target:
                check = tuple(sorted(path))
                if check not in map:
                    map[check] = 1
                    possible.append(path[:])
                return
            if _sum > target:
                return

            for i in range(len(candidates)):
                _sum += candidates[i]
                path.append(candidates[i])
                choose(_sum,path)
                _sum -= candidates[i]
                path.pop()
        
        choose(0,[])
        return possible
            

