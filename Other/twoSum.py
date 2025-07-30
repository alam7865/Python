def solve(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in seen:
            return [seen[diff], i]

        seen[nums[i]] = i


# def solve(nums, target):
#     set1 = set()
#     for i in range(len(nums)):
#         diff = target - nums[i]

#         if diff in set1:
#             print(diff, nums[i])

#         set1.add(nums[i])


nums = [2, 7, 11, 15, 2, 7, 2, 7]
target = 9

ans = solve(nums, target)
print("Result: ", ans)

solve(nums, target)
