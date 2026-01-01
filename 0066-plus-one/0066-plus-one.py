class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = ""
        for i in range(len(digits)):
            integer+=str(digits[i])
        integer = int(integer)+1
        liste = []
        for num in str(integer):
            liste.append(int(num))
        return liste

        