class Solution:
    def maxFreqSum(self, s: str) -> int:
        vm = 0
        cm = 0
        vowels = "aeiou"
        map = Counter(s)
        for char in s:
            if char in vowels:
                vm = max(vm,map[char])
            else:
                cm = max(cm,map[char])
        return vm+cm

        