# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
from sys import *

def main():
    """Implement the calculator"""
    if '+' in sys.argv[2]:
        result = int(sys.argv[1])+int(sys.argv[3])
        return result
    if '*' in sys.argv[2]:
        result = int(sys.argv[1])*int(sys.argv[3])
        return result
    if '-' in sys.argv[2]:
        result = int(sys.argv[1]) - int(sys.argv[3])
        return result
# YOUR CODE HERE

if __name__ == "__main__":
    print(main())
