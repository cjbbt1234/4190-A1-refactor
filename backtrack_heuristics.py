from helper_method import *

LIMIT = 2


@Counter
def back_track_heuristic_one(sol, iterator, blocks, length):
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
            if sol.is_consistent(LIMIT):  # if current assigned stars are consistent
                temp = back_track_heuristic_one(sol, iterator + 1, blocks, length)
                if temp is not None:
                    result = temp
                    break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result


@Counter
def back_track_heuristic_two(sol, iterator, blocks, length):
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
            if sol.is_consistent(LIMIT):  # if current assigned stars are consistent
                temp = back_track_heuristic_two(sol, iterator + 1, blocks, length)
                if temp is not None:
                    result = temp
                    break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result


@Counter
def back_track_heuristic_hybrid(sol, iterator, blocks, length):
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
            if sol.is_consistent(LIMIT):  # if current assigned stars are consistent
                temp = back_track_heuristic_hybrid(sol, iterator + 1, blocks, length)
                if temp is not None:
                    result = temp
                    break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result
