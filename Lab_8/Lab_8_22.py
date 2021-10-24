def in_order(nums):
    for pos, num in enumerate(nums):
        if pos < len(nums) - 1:
            if num > nums[pos + 1]:
                return False
    else:
        return True


# Type your code here.

if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')

    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')