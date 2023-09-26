def twoSum(nums, target: int):
    prevMap = {} # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return []              # this line is not really necessary, assuming that exactly one answer exists in the list


if __name__ == '__main__':
    print(twoSum([1,3], 4))
    print(twoSum([1,3,5,7], 12))
    print(twoSum([1,3,12,-6], 6))
    print(twoSum([5,10,20], 1111))
    print(twoSum([5,10,20], 15))

