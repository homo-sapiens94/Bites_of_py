def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    lst= []
    for index,number in enumerate(numbers):
    	matching_num = target-number
    	if matching_num in numbers[index+1:] and number < matching_num:
    		lst.append((index,numbers.index(target-number)))

    if lst==[]:
    	return None
    temp=lst[0]
    for i,j in lst[1:]:
    	if numbers[i]<numbers[temp[0]]:
    		temp = (i,j)
    return(temp)




##Pybites Solution



def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    nums = sorted(numbers)
    i = 0
    j = len(numbers) - 1
    while i < j:
        total = nums[i] + nums[j]
        if total < target:
            i += 1
        elif total > target:
            j -= 1
        else:
            index1 = numbers.index(nums[i])
            index2 = numbers.index(nums[j])
            return index1, index2
    return None



    