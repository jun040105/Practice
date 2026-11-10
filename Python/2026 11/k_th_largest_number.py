def find_kth_largest(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k-1]