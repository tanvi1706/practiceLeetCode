class Solution:
    def removeInvalidParentheses(self, s):
        left = 0
        right = 0
        for char in s:
            if char == "(":
                left += 1
            elif char == ")":
                right = right + 1 if left == 0 else right
                left  = left - 1 if left > 0 else left
        results = {}
        def recurse(s, index, left_count, right_count, miss_left, miss_right, e):
            if index == len(s):
                if miss_left == 0 and miss_right == 0:
                    results["".join(e)] = 1
            else:
                if (s[index] == "(" and miss_left > 0) or (s[index] == ")" and miss_right > 0):
                    recurse(s, index+1, left_count, right_count, miss_left - (s[index] == "("), miss_right - (s[index] == ")"), e)
                e.append(s[index])
                if s[index] != "(" and s[index] != ")":
                    recurse(s, index + 1, left_count, right_count, miss_left, miss_right, e)
                elif s[index] == "(":
                    recurse(s, index + 1, left_count + 1, right_count, miss_left, miss_right)
                elif s[index == ")"] and left_count > right_count:
                    recurse(s, index + 1, left_count, right_count + 1, miss_left, miss_right, e)
                e.pop()

        recurse(s, 0, 0, 0 ,left, right, [])
        return list(results.keys())
 


