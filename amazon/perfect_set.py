"""
https://leetcode.com/discuss/interview-question/4628170/Amazon-OA
"""

def max_size_perfect_set(nums: list[int]) -> int:
    res = 0
    set_nums = set(nums)

    for num in nums:
        curr_size = 1
        while num*num in set_nums:
            curr_size += 1
            num *= num
        res = max(res, curr_size)

    if res >= 2: return res
    return 0

nums = [625, 2, 4, 256, 16, 5, 25]
res = max_size_perfect_set(nums)
print(res)