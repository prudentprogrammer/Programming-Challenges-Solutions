# Link: https://uva.onlinejudge.org/external/4/482.pdf
test_cases = int(input())
for i in range(test_cases):
    blank_line = input()
    perm_array = [int(x) for x in input().split()]
    nums = input().split()
    res = [''] * len(nums)

    for curr_index, perm_index in enumerate(perm_array):
        res[perm_index - 1] = nums[curr_index]

    for num in res:
        print(num)

    # Don't print for the last instance of the problem
    if i != test_cases - 1:
        print()
