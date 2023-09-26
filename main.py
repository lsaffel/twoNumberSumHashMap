def twoSum(nums, target: int):
    prevMap = {}        # value : index
    for i, n in enumerate(nums):        # i is the index of n, n is the value in nums
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
        print(prevMap)      # just to show how this program works. Not a necessary line
    return []              # this line is not really necessary, assuming that exactly one answer exists in the list


if __name__ == '__main__':
    print(twoSum([1,3], 4))
    print("///////////////////////////////////////////")
    print(twoSum([1,3,5,7], 12))
    print("///////////////////////////////////////////")
    print(twoSum([1,3,12,-6], 6))
    print("///////////////////////////////////////////")
    print(twoSum([5,10,20], 1111))
    print("///////////////////////////////////////////")
    print(twoSum([5,10,20], 15))

