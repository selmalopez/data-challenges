'''Implement basic stat Functions'''
import statistics

def my_mean(samples):
    '''returns the mean of the observations'''
    return sum(samples) / len(samples)


def my_standard_deviation(samples):
    '''returns the standard deviation of the observations'''
    return statistics.stdev(samples)

def my_mode(samples):
    '''returns the mode of the observations'''
    return statistics.mode(samples)



def my_multimodes(samples):
    '''returns the modes of the observations as a sorted list'''
    return statistics.multimode(samples)


def my_median(samples):
    '''returns the median of the observations as a sorted list'''
    return statistics.median(samples)
