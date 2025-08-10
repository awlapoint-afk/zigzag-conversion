class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        row_inc = True
        result_dict = {}
        result = ""

        row = col = 0
        for c in s:
            print(f"row = {row}, col = {col} c = {c}")
            result_dict[(row,col)] = c
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

        result_list = list(result_dict.keys())
        result_list.sort()
        for value in result_list:
            result += result_dict[value]

        return result


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