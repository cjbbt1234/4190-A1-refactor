import math


def get_blocks(file_name):
    """Read file to generate a 2d list

    :param file_name: Name of file
    :return: Return a 2d list that every list in main list contains its blocks' number
    """

    f = open(file_name, 'r')
    result = []
    for lines in f:
        index = lines.find('t')  # find first number
        block = list(map(int, lines[index + 1:len(lines)].split(',')))
        result.append(block)
    return result


def get_size(lists):
    """Get size of 2d array, in this assignment, is to get how many cells in total

    :param lists: A 2d list
    :return: Return how many numbers are in lists
    """

    size = 0
    for block in lists:
        size += len(block)
    return size


def get_length(size):
    """Get the length of puzzle, a 8x8=64 puzzle has length 8

    :param size: Size of puzzle
    :return: Return the length of puzzle
    """

    return int(math.sqrt(size))
