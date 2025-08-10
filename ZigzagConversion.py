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
        row_inc = True
        result_list = [None] * s_len

        row = col = 0
        for index, c in enumerate(s):
            result_list[index] = (row, col, c)
            if row_inc:
                row += 1
                if row == numRows:
                    row_inc = False
                    row -= 1
            if not row_inc:
                row -= 1
                col += 1
                if row < 0:
                    row_inc = True
                    row = 1

        result_list.sort()
        return ''.join(value[2] for value in result_list)


solution = Solution()

# test case 1
test1 = solution.convert("PAYPALISHIRING", 3)
test1_pass = "PAHNAPLSIIGYIR"
if test1 == test1_pass:
    print("TEST1 => PASS")
else:
    print(f"TEST1 => FAIL {test1} not {test1_pass}")

# test case 2
test2 = solution.convert("PAYPALISHIRING", 4)
test2_pass = "PINALSIGYAHRPI"
if test2 == test2_pass:
    print("TEST2 => PASS")
else:
    print(f"TEST2 => FAIL {test2} not {test2_pass}")

# test case 3
test3 = solution.convert("A", 1)
if test3 == "A":
    print("TEST3 => PASS")
else:
    print("TEST3 => FAIL")