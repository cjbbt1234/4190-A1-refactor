import random
from itertools import combinations
from helper_method import *

LIMIT = 2


def back_track_heuristic_one(sol, iterator, blocks, length):
    """This method solve the star battle with heuristic 1

    :param sol:solution of star battle
    :param iterator:record which block we are working on
    :param blocks:blocks information, is a 2d list
    :param length: length of star battle map, 8x8 map has length 8
    :return:return solution of star battle
    """

    result = None
    # ###########################################
    # from star_list import StarList  #
    # sol = StarList()  #
    # ##################################
    if sol.get_size() == sol.get_count():
        result = sol
    else:
        min_length = float('inf')
        min_index = -1
        min_array = []
        for i in range(int(sol.get_count() / 2), length):
            if len(blocks[i]) < min_length:
                min_length = len(blocks[i])
                min_array = []
                min_array.append(i)
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
                remove_neighbors(position_two, temp_copy, length)
                remove_col_and_row(sol, temp_copy, length)
                if check_remain_domain(sol, temp_copy):
                    temp = back_track_heuristic_one(sol, iterator + 1, temp_copy, length)
                    if temp is not None:
                        result = temp
                        break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result


def back_track_heuristic_two(sol, iterator, blocks, length):
    """This method solve the star battle with heuristic 2

    :param sol:solution of star battle
    :param iterator:record which block we are working on
    :param blocks:blocks information, is a 2d list
    :param length: length of star battle map, 8x8 map has length 8
    :return:return solution of star battle
    """

    result = None
    print(sol)
    # ###########################################
    # from star_list import StarList  #
    # sol = StarList()  #
    # ##################################
    if sol.get_size() == sol.get_count():
        result = sol
    else:
        candidate = list(combinations(blocks[iterator], 2))
        candidate = sort_candidate(candidate,blocks,length,iterator)
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
                remove_neighbors(position_two, temp_copy, length)
                remove_col_and_row(sol, temp_copy, length)
                if check_remain_domain(sol, temp_copy):
                    temp = back_track_heuristic_two(sol, iterator + 1, temp_copy, length)
                    if temp is not None:
                        result = temp
                        break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result


def back_track_heuristic_hybrid(sol, iterator, blocks, length):
    """This method solve the star battle with heuristic 1

    :param sol:solution of star battle
    :param iterator:record which block we are working on
    :param blocks:blocks information, is a 2d list
    :param length: length of star battle map, 8x8 map has length 8
    :return:return solution of star battle
    """

    result = None
    # ###########################################
    # from star_list import StarList  #
    # sol = StarList()  #
    # ##################################
    if sol.get_size() == sol.get_count():
        result = sol
    else:
        min_length = float('inf')
        min_index = -1
        min_array = []
        for i in range(int(sol.get_count() / 2), length):
            if len(blocks[i]) < min_length:
                min_length = len(blocks[i])
                min_array = []
                min_array.append(i)
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
        candidate = sort_candidate(candidate,blocks,length,iterator)
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
                remove_neighbors(position_two, temp_copy, length)
                remove_col_and_row(sol, temp_copy, length)
                if check_remain_domain(sol, temp_copy):
                    temp = back_track_heuristic_hybrid(sol, iterator + 1, temp_copy, length)
                    if temp is not None:
                        result = temp
                        break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result



##############################################################
from star_list import StarList
import test
import draw

def tests():
    i = [[43, 44, 36, 51, 35, 34, 42], [30, 29, 21, 13, 22, 14, 5], [8, 16, 24, 23, 7, 15, 6],
         [45, 53, 46, 37, 38, 54, 62, 63], [58, 57, 59, 60, 50, 52, 49, 61, 41, 33],
         [56, 48, 55, 40, 64, 39, 32, 31, 47], [20, 28, 27, 12, 11, 4, 3], [10, 18, 26, 19, 25, 2, 9, 17, 1]]
    # print(i)
    for i in test.ten_hundred[0:1]:
        sol = StarList(10 * 2)
        result = back_track_heuristic_hybrid(sol, 0, i, 10)
        # draw.draw_solution(i,result.get_solution_list())
        if result is None:
            print('bad')
    print('finish')

tests()
###############################
