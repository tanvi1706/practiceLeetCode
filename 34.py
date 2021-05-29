def searchRange(self, nums: List[int], target: int) -> List[int]:
    low = self.Bound(nums, target, True)
    if low == -1:
        return [-1, -1]
    upp = self.Bound(nums, target, False)
    return [low, upp]
def Bound(self, nums: list[int], target: int, isFirst: bool):
    N = len(nums)
    begin, end = 0, N - 1
    while begin <= end:
        mid = int((begin + end) / 2)
        if nums[mid] == target:
            if isFirst:
                if mid == begin or nums[mid - 1] != target:
                    return mid
                end = mid - 1
            else:
                if mid == end or nums[mid + 1] != target:
                    return mid
                begin = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            begin = mid + 1
    return -1