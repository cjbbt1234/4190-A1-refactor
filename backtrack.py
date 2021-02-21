from star_list import StarList
from itertools import combinations
from helper_method import *

LIMIT=2

def back_track(sol, iterator, blocks, length):
    """This method do back trace to solve the puzzle

    :param sol:solution of star battle
    :param iterator:record which block we are working on
    :param blocks:blocks information, is a 2d list
    :param length: length of star battle map, 8x8 map has length 8
    :return:return solution of star battle
    """
    result=None
    # sol=StarList(sol)
    if sol.get_size()==sol.get_count():
        result=sol
    else:
        candidate=list(combinations(blocks[iterator],2))
        for i in candidate:
            index_one=iterator*2
            index_two=iterator*2+1
            (a,b)=i  #the get two cells in a block
            block_one=search_block_num(blocks,a)
            block_two=search_block_num(blocks,b)  # find which block a,b belongs to
            sol.set_star(index_one,a,block_one)
            sol.set_star(index_two,b,block_two)
            if sol.is_consistent(LIMIT):
                temp=back_track(sol,iterator+1,blocks,length)
                if temp is not None:
                    result=temp
                    break
            sol.reset_star(index_one)
            sol.reset_star(index_two)
    return result

def test():
    test_block=[[56, 55, 64, 63, 47], [31, 32, 24, 40, 39, 48, 30, 23], [49, 50, 42, 34, 57, 26, 27, 41, 33], [51, 59, 58, 60, 52, 43, 35], [62, 54, 53, 61, 45, 46, 37, 38, 36, 44, 28, 29], [9, 1, 10, 2, 17, 18, 25], [3, 4, 12, 13, 11, 21, 19, 20], [15, 14, 16, 6, 7, 8, 5, 22]]
    sol=StarList(8*2)
    result=back_track(sol,0,test_block,8)
    print(result.get_solution_list())
    print(sol)

test()

