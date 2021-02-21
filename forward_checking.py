

from helper_method import *

LIMIT = 2


@Counter
def forward_checking(sol, iterator, blocks, length):
    """This method do back track with forward checking to solve the puzzle

    :param sol:solution of star battle
    :param iterator:record which block we are working on
    :param blocks:blocks information, is a 2d list
    :param length: length of star battle map, 8x8 map has length 8
    :return:return solution of star battle
    """
    result = None
    if sol.get_size() == sol.get_count():
        result = sol
    else:
        candidate = list(combinations(blocks[iterator], 2))
        for i in candidate:
            index_one = iterator * 2
            index_two = iterator * 2 + 1
            (position_one, position_two) = i  # the get two cells in a block
            block_one = search_block_num(blocks, position_one)
            block_two = search_block_num(blocks, position_two)  # find which block a,b belongs to
            sol.set_star(index_one, position_one, block_one)
            sol.set_star(index_two, position_two, block_two)
            if sol.is_consistent(LIMIT):  # if current assigned stars are consistent
                temp_copy = deep_copy_2d(blocks)
                remove_neighbors(position_one, temp_copy, length)
                remove_neighbors(position_two, temp_copy, length)
                remove_col_and_row(sol, temp_copy, length)
                if check_remain_domain(sol, temp_copy):
                    temp = forward_checking(sol, iterator + 1, temp_copy, length)
                    if temp is not None:
                        result = temp
                        break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result
