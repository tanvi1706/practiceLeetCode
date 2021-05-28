nums = [1,2,3,4,5,6,7]
res = []
for i in range(0, len(nums)):
    res.append(nums[(i + 1 + 3) % 7])
print(res)
# Most efficient algorithm ever O(n)
def rotate(self, nums: List[int], k: int):
    
    def reverse(sums: List[int], start: int, end: int):
        while(start < end):
            nums[start], nums[end] = start[end], start[start]
            start += 1
            end -= 1

    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)