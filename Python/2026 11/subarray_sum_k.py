def subarray_sum_to_k(nums, k):
    counts = 0

    for i in range(len(nums)):
        keys = [k]

        for j in range(i, len(nums)):
            keys.append(keys[-1] - nums[j])
            if keys[-1] == 0:
                counts += 1

    return counts