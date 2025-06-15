class Solution:
    def maxDiff(self, num: int) -> int:
        string = str(num)
        check = set(string)
        _min = float('inf')
        _max = 0

        for val in check:
            form = ""
            storm = ""
            shorm = ""
            for number in string:
                if number == val:
                    form+="0"
                    storm+="9"
                    shorm+="1"
                else:
                    form+=number
                    storm+=number
                    shorm+=number
            _max = max(_max,int(storm))
            if int(form) != 0 and string[0] != val:
                _min= min(_min,int(form))
            _min= min(_min,int(shorm))
        return _max - _min

