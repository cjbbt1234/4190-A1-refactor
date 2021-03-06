
from helper_method import *

LIMIT = 2


@Counter
def forward_checking_heuristic_one(sol, iterator, blocks, length):
    """This method solve the star battle with heuristic 1

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
        candidate = h1_most_constrained(sol, iterator, blocks, length)
        for i in candidate:
            index_one = iterator * 2
            index_two = iterator * 2 + 1
            (position_one, position_two) = i  # the get two cells in a block
            block_one = search_block_num(blocks, position_one)
            block_two = search_block_num(blocks, position_two)  # find which block a,b belongs to
            sol.set_star(index_one, position_one, block_one)
            sol.set_star(index_two, position_two, block_two)
            if sol.is_consistent(LIMIT):
                temp_copy = deep_copy_2d(blocks)
                remove_neighbors(position_one, temp_copy, length)
                # discard position in other blocks which conflict with current assignment
                remove_neighbors(position_two, temp_copy, length)
                remove_col_and_row(sol, temp_copy, length)
                if check_remain_domain(sol, temp_copy):
                    # check if other unsigned blocks are still have position to put their stars
                    temp = forward_checking_heuristic_one(sol, iterator + 1, temp_copy, length)
                    if temp is not None:
                        result = temp
                        break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result


@Counter
def forward_checking_heuristic_two(sol, iterator, blocks, length):
    """This method solve the star battle with heuristic 2

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
        candidate = h2_most_constraining(candidate, blocks, length, iterator)
        for i in candidate:
            index_one = iterator * 2
            index_two = iterator * 2 + 1
            (position_one, position_two) = i  # the get two cells in a block
            block_one = search_block_num(blocks, position_one)
            block_two = search_block_num(blocks, position_two)  # find which block a,b belongs to
            sol.set_star(index_one, position_one, block_one)
            sol.set_star(index_two, position_two, block_two)
            if sol.is_consistent(LIMIT):
                temp_copy = deep_copy_2d(blocks)
                remove_neighbors(position_one, temp_copy, length)
                # discard position in other blocks which conflict with current assignment
                remove_neighbors(position_two, temp_copy, length)
                remove_col_and_row(sol, temp_copy, length)
                if check_remain_domain(sol, temp_copy):
                    # check if other unsigned blocks are still have position to put their stars
                    temp = forward_checking_heuristic_two(sol, iterator + 1, temp_copy, length)
                    if temp is not None:
                        result = temp
                        break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result


@Counter
def forward_checking_heuristic_hybrid(sol, iterator, blocks, length):
    """This method solve the star battle with heuristic 1

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
        candidate = h1_most_constrained(sol, iterator, blocks, length)
        candidate = h2_most_constraining(candidate, blocks, length, iterator)
        for i in candidate:
            index_one = iterator * 2
            index_two = iterator * 2 + 1
            (position_one, position_two) = i  # the get two cells in a block
            block_one = search_block_num(blocks, position_one)
            block_two = search_block_num(blocks, position_two)  # find which block a,b belongs to
            sol.set_star(index_one, position_one, block_one)
            sol.set_star(index_two, position_two, block_two)
            if sol.is_consistent(LIMIT):
                temp_copy = deep_copy_2d(blocks)
                remove_neighbors(position_one, temp_copy, length)
                # discard position in other blocks which conflict with current assignment
                remove_neighbors(position_two, temp_copy, length)
                remove_col_and_row(sol, temp_copy, length)
                if check_remain_domain(sol, temp_copy):
                    # check if other unsigned blocks are still have position to put their stars
                    temp = forward_checking_heuristic_hybrid(sol, iterator + 1, temp_copy, length)
                    if temp is not None:
                        result = temp
                        break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result
