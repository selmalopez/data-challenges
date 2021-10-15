import statistics

def my_mean(samples):
    return sum(samples) / len(samples)
    '''returns the mean of the observations'''
    # YOUR CODE HERE


def my_standard_deviation(samples):
    return statistics.stdev(samples)
    '''returns the standard deviation of the observations'''
    # YOUR CODE HERE

def my_mode(samples):
    return statistics.mode(samples)
    '''returns the mode of the observations'''
    # YOUR CODE HERE


def my_multimodes(samples):
    return statistics.multimode(samples)
    '''returns the modes of the observations as a sorted list'''
    # YOUR CODE HERE


def my_median(samples):
   return statistics.median(samples)

    # YOUR CODE HERE
