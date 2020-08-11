from typing import List


class Solution:
    # brute
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            ans = self.generateParenthesis(n - 1)
            newAns = []
            for s in ans:
                for i in range(len(s) + 1):
                    newS = s[:i] + "()" + s[i:]
                    if newS not in newAns: newAns.append(newS)
            return newAns

    # backtracking
    def generateParenthesis1(self, n):

        def paren(left, right, curr, res):
            # 'evaluate current string
            # if we are out of brackets to add, we must be at a valid string
            if left == 0 and right == 0:
                res.append(curr)
                return

            # recursive call: add either open or close
            # if adding open bracket is valid
            if left > 0:
                # add open bracket, decr count
                paren(left - 1, right, curr + "(", res)

            # if adding close bracket is valid
            if right > left:
                # add close bracket, decr count
                paren(left, right - 1, curr + ")", res)

            return res

        # end paren()

        res = paren(n, n, '', [])

        return res


s = Solution()
print(s.generateParenthesis(3))
