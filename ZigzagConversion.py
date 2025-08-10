class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        s_len = len(s)
        result = ""

        if numRows == 3:
            steps = [(0,4), (1,2), (2,4)]
        else:
            return None

        for step in steps:
            i = step[0]
            j = step[1]
            while i <= s_len - 1:
                result += s[i]
                i += j

        return result


solution = Solution()

# test case 1
test1 = solution.convert("PAYPALISHIRING", 3)
if test1 == "PAHNAPLSIIGYIR":
    print("TEST1 => PASS")
else:
    print("TEST1 => FAIL")

# test case 2
test2 = solution.convert("PAYPALISHIRING", 4)
if test2 == "PINALSIGYAHRPI":
    print("TEST2 => PASS")
else:
    print("TEST2 => FAIL")

# test case 3
test3 = solution.convert("A", 1)
if test3 == "A":
    print("TEST3 => PASS")
else:
    print("TEST3 => FAIL")