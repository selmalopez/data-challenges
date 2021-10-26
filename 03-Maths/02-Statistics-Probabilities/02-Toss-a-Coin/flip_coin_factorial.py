# pylint: disable=missing-docstring

import math
from math import factorial


def count_possibilities(n_toss, n_heads):
    '''TO DO: '''
    return factorial(n_toss) / (factorial(n_heads)*factorial(n_toss-n_heads))
count_possibilities(4,2)


def count_total_possibilities(n_toss):
    '''TO DO: '''
    return 2 **(n_toss)
    # YOUR CODE HERE


def probability(n_toss):
    '''TO DO: '''
    dict_i = {}
    for n_heads in range(n_toss+1):
        dict_i[n_heads] = count_possibilities(n_toss,n_heads) / count_total_possibilities(n_toss)
    print(dict_i)
probability(2)
