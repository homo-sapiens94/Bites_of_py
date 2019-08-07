def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    lst=[]
    total=0
    for i, value in enumerate(sequence):
        total+=value
        average=total/(i+1)
        lst.append((round(average,2)))
    return lst




#Pybites Solution using itertools.accumulate


def running_mean(sequence):
    """Same functionality as above but using itertools.accumulate
       and turning it into a generator"""
    for i, num in enumerate(accumulate(sequence), 1):
        yield round(num/i, 2)


