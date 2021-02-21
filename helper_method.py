import random
from itertools import combinations

import math


class Counter(object):
    """
    use to counter number node iterated
    """

    def __init__(self, fun):
        self._fun = fun
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self._fun(*args, **kwargs)


def search_block_num(blocks, position):
    """find which block the position belongs to

    :param blocks: a 2d list contains all blocks
    :param position: position of a cell
    :return: return the index the position belongs to
    """
    result = -1
    for i in range(len(blocks)):
        temp = blocks[i]
        if position in temp:
            result = i
    return result


def deep_copy_2d(blocks):
    """deep copy of 2d list

    :param blocks: a 2d list contains blocks of puzzle
    :return: return a deep copied list
    """
    result = []
    for i in blocks:
        temp = []
        for j in i:
            temp.append(j)
        result.append(temp)
    return result


def remove_neighbors(index, block, length):
    """remove all neighbors cell around star

    :param index: index of cell
    :param block: the 2d list
    :param length: length of the puzzle, 8x8 puzzle has length 8
    :return: return the trimmed block list
    """
    if index % length == 1:  # left edge
        neighbor = [index - length, index - length + 1, index + 1, index + length, index + length + 1]
    elif index % length == 0:  # right edge
        neighbor = [index - length, index - length - 1, index - 1, index + length, index + length - 1]
    else:
        neighbor = [index - length, index - length - 1, index - 1, index + length, index + length - 1,
                    index - length + 1,
                    index + 1, index + length + 1]
    for i in neighbor:
        for j in block:
            if i in j:
                j.remove(i)
    return block


def remove_col_and_row(sol, block, length):
    """remove all cells in that col/row if that col/row has two stars

    :param sol: current solution to star battle
    :param block: the 2d list
    :param length: length of the puzzle, 8x8 puzzle has length 8
    :return: no return
    """
    row_count = []
    col_count = []
    for i in range(length):
        row_count.append(0)  # count how many stars in each row
        col_count.append(0)  # count how many stars in each column
    for index in range(sol.get_count()):
        star = sol.get_star(index)
        pos = star.get_position()
        row = int((pos - 1) / length)
        col = int((pos - 1) % length)
        row_count[row] += 1
        col_count[col] += 1
    for i in range(length):  # remove all cells in row if this row has two stars
        if row_count[i] == 2:
            elements = list(range(i * length + 1, i * length + length + 1))
            for j in elements:
                for l in block:
                    if j in l:
                        l.remove(j)
    for i in range(length):  # remove all cells in column if this column has two stars
        if col_count[i] == 2:
            elements = list(range(i + 1, length * length + 1, length))
            for j in elements:
                for l in block:
                    if j in l:
                        l.remove(j)


# def check_remain_domain(sol, block):
#     result = True
#     length = int(sol.get_size() / 2)
#     un_sign_block = sol.get_count()
#     for i in range(un_sign_block, length):
#         domain_count = len(block[i])
#         if domain_count > 0:
#             min_value = min(block[i])
#             curr_block = block[i]
#             if domain_count <= 2 and min_value+1 in curr_block:
#                 result = False
#                 break
#             elif domain_count >= 5:
#                 continue
#             else:
#                 if domain_count == 3:
#                     if (min_value + 1 in curr_block and (
#                             min_value + length in curr_block or min_value + length + 1 in curr_block)):
#                         result = False
#                         break
#                     elif (min_value + length in block[i] and (
#                             min_value + length - 1 in curr_block or min_value + length + 1 in curr_block)):
#                         result = False
#                         break
#                 elif domain_count == 4:
#                     if (
#                             min_value + 1 in curr_block and min_value + length in curr_block and min_value + length + 1 in curr_block):
#                         result = False
#                         break
#         else:
#             result = False
#             break
#     return result


def check_remain_domain(sol, block):
    result = True
    length = int(sol.get_size() / 2)
    un_sign_block = sol.get_count()
    for i in range(un_sign_block, length):
        domain_count = len(block[i])
        if domain_count >= 5:
            continue
        elif domain_count <= 1:
            result = False
            break
        else:
            min_value = min(block[i])
            curr_block = block[i]
            right = math.ceil(min_value / length) == math.ceil((min_value + 1) / length) and min_value + 1 in curr_block
            down = min_value + length in curr_block
            down_left = math.ceil((min_value + length - 1) / length) == math.ceil(
                (min_value + length) / length) and min_value + length - 1 in curr_block
            down_right = math.ceil((min_value + length + 1) / length) == math.ceil(
                (min_value + length) / length) and min_value + length + 1 in curr_block
            if domain_count == 2:
                if right or down:
                    result = False
                    break
            elif domain_count == 3:
                if down:
                    if right or down_left or down_right:
                        result = False
                        break
                elif down_right and right:
                    result = False
                    break
            elif domain_count == 4:
                if right and down and down_right:
                    result = False
                    break
    return result


def get_neighbor(position, length):
    """gives neighbors of a given position

    :param position: position of cells
    :param length: length of star battle map, 8x8 map has length 8
    :return: a list of neighbor cells
    """
    list = None
    up = position - length
    down = position + length
    right = position + 1
    left = position - 1
    upleft = position - length - 1
    upright = position - length + 1
    downleft = position + length - 1
    downright = position + length + 1
    if position == 1:
        list = [right, down, downright]
    elif position == length:
        list = [left, downleft, down]
    elif position == length * length - length + 1:
        list = [up, upright, right]
    elif position == length * length:
        list = [left, up, upleft]
    elif position % length == 1:  # left edge
        list = [up, upright, right, down, downright]
    elif position % length == 0:  # right edge
        list = [up, upleft, left, downleft, down]
    elif position > 1 and position < length:  # first row
        list = [left, downleft, down, downright, right]
    elif position < length * length and position > length * length - length + 1:
        list = [left, upleft, up, upright, right]
    else:
        list = [up, upright, upleft, left, right, down, downleft, downright]
    return list


def h1_most_constrained(sol, iterator, blocks, length):
    min_length = float('inf')
    min_index = -1
    min_array = []
    for i in range(int(sol.get_count() / 2), length):
        if len(blocks[i]) < min_length:
            min_length = len(blocks[i])
            min_array = [i]
            min_index = i
        elif len(blocks[i]) == min_length:
            min_array.append(i)
    new_index = random.choice(min_array)
    if iterator != new_index:
        swap_a = blocks[new_index]
        swap_b = blocks[iterator]
        blocks[iterator] = swap_a
        blocks[new_index] = swap_b
    candidate = list(combinations(blocks[iterator], 2))
    return candidate


def h2_most_constraining(candidate, blocks, length, iterator):
    """this method sort candidates by how many cell(options) they will remove

    :param candidate: candidate turple list
    :param blocks: blocks information, is a 2d list
    :param length: length of star battle map, 8x8 map has length 8
    :param iterator: record which block we are working on
    :return: a sorted candidates list
    """
    candidate_sort = []
    for can in candidate:
        (position_x, position_y) = can
        row = set()
        col = set()
        # if same row:
        if int((position_x - 1) / length) == int((position_y - 1) / length):
            r = int((position_x - 1) / length)
            row = set(range(r * length + 1, r * length + length + 1))
        # if same col
        if (position_x - 1) % length == (position_y - 1) % length:
            c = (position_x - 1) % length
            col = set(range(c + 1, length * length + 1, length))
        # get all neighbor of position_x and position_y
        neighborX = set(get_neighbor(position_x, length))
        neighborY = set(get_neighbor(position_y, length))
        u = row.union(col).union(neighborX).union(neighborY)
        all = list(u)
        countInBlock = 0
        countAllBlock = 0
        for i in all:
            if i in blocks[iterator]:
                countInBlock += 1
            for j in blocks:
                if i in j:
                    countAllBlock += 1
                    break
        candidate_sort.append((can, countAllBlock - countInBlock))
    sortedCand = sorted(candidate_sort, key=lambda x: x[1])
    for i in range(len(sortedCand) - 1):
        j = i + 1
        if sortedCand[i][1] == sortedCand[j][1]:
            if random.random() > 0.5:
                temp = sortedCand[i]
                sortedCand[i] = sortedCand[j]
                sortedCand[j] = temp
    result = []
    for i in sortedCand:
        result.append(i[0])
    return result
