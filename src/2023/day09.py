from functools import reduce


def p1(lines):
    ans = 0
    for line in lines:
        nums = list(map(lambda x: int(x), line.split()))
        last_list = [nums[-1]]
        while sum(nums) != 0:
            new_nums = []
            for i in range(1, len(nums)):
                new_nums.append(nums[i] - nums[i-1])
            last_list.append(new_nums[-1])
            nums = new_nums
        ans += reduce(lambda a, b: a+b, last_list)
    return ans


def p2(lines):
    ans = 0
    for line in lines:
        nums = list(map(lambda x: int(x), line.split()))
        first_list = [nums[0]]
        while sum(nums) != 0:
            new_nums = []
            for i in range(1, len(nums)):
                new_nums.append(nums[i] - nums[i - 1])
            first_list.insert(0, new_nums[0])
            nums = new_nums

        value = reduce(lambda a, b: b - a, first_list)
        ans += value
    return ans
