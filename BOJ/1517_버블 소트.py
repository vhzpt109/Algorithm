def bubble_sort(nums):
    swap_count = 0
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap_count += 1
    return swap_count


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    print(bubble_sort(nums))