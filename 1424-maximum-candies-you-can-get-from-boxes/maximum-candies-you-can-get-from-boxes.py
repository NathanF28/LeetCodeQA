class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        opened = set()
        key_list= set()
        total = 0 

        def bfs(boxes):
            nonlocal opened
            nonlocal total
            nonlocal key_list
            next = []
            for box in boxes:
                if status[box] and box not in opened and box in key_list:
                    total+= candies[box]
                    opened.add(box)
                    for key in keys[box]:
                        if key not in opened:
                            next.append(key)
                            status[key] = 1
                    for neighbor in containedBoxes[box]:
                        if neighbor not in opened:
                            key_list.add(neighbor)
                            next.append(neighbor)
            if len(next):
                bfs(next)
        for box in initialBoxes:
            key_list.add(box)
        bfs(initialBoxes)
        return total