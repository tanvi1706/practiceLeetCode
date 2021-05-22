class Solution:
    def AdditiveNumber(self,num: str) -> bool:

        def backtrack(self, num1: str, num2: str, rem: str) -> bool:
            if not rem:
                return True
            target = str(int(num1) + int(num2))
            if rem.startswith(target) and all(str(int(x)) == x for x in (num1, num2)):
                return backtrack(num2, target, rem[len(target):])
            return False

        for i in range(2, len(num)):
            for j in range(1,i):
                if len(num) - i >= j and len(num) - i >= i - j:
                    if backtrack(num[:j], num[j:i], num[i:]):
                        return True
                        break
        return False