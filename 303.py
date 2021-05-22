class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.summ = [0,]
        for x in range(0, len(self.nums)):
            self.summ.append(self.nums[x] + self.summ[x])

    def sumRange(self, left: int, right: int) -> int:
        return self.summ[right + 1] - self.summ[left]





# class NumArray:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
    
#     def sumRange(self, left: int, right: int) -> int:
#         summ = 0
#         for x in range(left, right + 1):
#             summ += self.nums[x]

#         return summ



