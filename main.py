from draw import *
from star_list import *
import timeit
from read import *
import multiprocessing
from backtrack import back_track
from backtrack_heuristics import *
from forward_checking import forward_checking
from forward_checking_heuristics import *

"""
Course: COMP 4190 Artificial Intelligence by Cuneyt Gurcan Akcora, University of Manitoba, Canada
Assignment: Constraint Satisfaction Problem – 2-Star Puzzles
Date: Feb.22 2021
Project aim:
This project is use to solve 2-star star battle and investigate efficiency of backtrack and forward checking algorithm.
Project author:
    Group 6:
    Siyuan Shang, id 7812442
    Yubo Chen, id 7811477
"""

WAIT_TIME = 600  # The time of wait the algorithm to solve a puzzle
LIMIT = 2  # Number of stars in row,column and blocks


def back_track_std(solution, blocks, length):
    """
    Function caller
    :param solution: the star solution list (empty here)
    :param blocks: the list contain all blocks
    :param length: the side length of the puzzle
    :return: the iteration counter on recursion
    """
    back_track.counter = 0
    back_track(solution, 0, blocks, length)
    return back_track.counter


def back_track_h1(solution, blocks, length):
    """
    Function caller
    """
    back_track_heuristic_one.counter = 0
    back_track_heuristic_one(solution, 0, blocks, length)
    return back_track_heuristic_one.counter


def back_track_h2(solution, blocks, length):
    """
    Function caller
    """
    back_track_heuristic_two.counter = 0
    back_track_heuristic_two(solution, 0, blocks, length)
    return back_track_heuristic_two.counter


def back_track_hybrid(solution, blocks, length):
    """
    Function caller
    """
    back_track_heuristic_hybrid.counter = 0
    back_track_heuristic_hybrid(solution, 0, blocks, length)
    return back_track_heuristic_hybrid.counter


def forward_check_std(solution, blocks, length):
    """
    Function caller
    """
    forward_checking.counter = 0
    forward_checking(solution, 0, blocks, length)
    return forward_checking.counter


def forward_check_h1(solution, blocks, length):
    """
    Function caller
    """
    forward_checking_heuristic_one.counter = 0
    forward_checking_heuristic_one(solution, 0, blocks, length)
    return forward_checking_heuristic_one.counter


def forward_check_h2(solution, blocks, length):
    """
    Function caller
    """
    forward_checking_heuristic_two.counter = 0
    forward_checking_heuristic_two(solution, 0, blocks, length)
    return forward_checking_heuristic_two.counter


def forward_check_hybrid(solution, blocks, length):
    """
    Function caller
    """
    forward_checking_heuristic_hybrid.counter = 0
    forward_checking_heuristic_hybrid(solution, 0, blocks, length)
    return forward_checking_heuristic_hybrid.counter


def solve_puzzle(length, blocks, fnc):
    """
    solve the puzzle use fnc algorithm

    :param length: the side length of the puzzle
    :param blocks: the list contain all blocks
    :param fnc: the function name will ues in solve the puzzle
    :return:
    """
    solution = StarList(length * 2)
    start = timeit.default_timer()  # set up the timer
    iteration = fnc(solution, blocks, length)  # solve the puzzle use fnc, get the iteration
    stop = timeit.default_timer()
    print(fnc.__name__, ': Time cost: ', stop - start, 'second')
    print('Have', iteration, 'iterations')
    if solution.get_count() == length * 2:
        print('Solution is:', solution.get_solution_list())
        draw_solution(blocks, solution.get_solution_list())
        # Draw the puzzle and solution in UI, please remember the time you watch the result will also count in total
        # running time of the process. This will cause abort from process when the UI display time reach 10 minute.
        # But the display time will not count in recursion time. When you close the UI, it will return and go for next.
    else:
        print('No Solution found !')


def process_solve_puzzle(length, blocks, fnc):
    """
    make a process to count the time of solving puzzle, and when it is timeout kill it

    :param length: the side length of the puzzle
    :param blocks: the list contain all blocks
    :param fnc: the function name will ues in solve the puzzle
    :return:
    """
    process = multiprocessing.Process(target=solve_puzzle, args=(length, blocks, fnc,))

    process.start()

    process.join(WAIT_TIME)

    if process.is_alive():
        print(fnc.__name__, " get stuck ... let's kill it...No solution")
        print("Or it may because you keep the puzzle UI open for a long time and it reach the time limit...")
        print()
        print()
        process.kill()
        process.join()


# main
#######################################################################################################################

if __name__ == '__main__':

    print("Program start...")

    file_name_1 = "grid8x8.txt"
    file_name_2 = "grid10x10.txt"
    file_name_3 = "grid14x14.txt"

    file_list = [file_name_1, file_name_2, file_name_3]

    for curr_puzzle in file_list:
        print("Begin to solve ", curr_puzzle)

        puzzle = get_blocks(curr_puzzle)
        size = get_size(puzzle)
        side_length = get_length(size)

        process_solve_puzzle(side_length, puzzle, forward_check_hybrid)
        # solve the puzzle use backtrack extended to forward checking with hybrid heuristics, the fast one

        # if you want to try other algorithms, just uncomment the algorithm you want to test
        # process_solve_puzzle(side_length, puzzle, back_track_std)
        # process_solve_puzzle(side_length, puzzle, back_track_h1)
        # process_solve_puzzle(side_length, puzzle, back_track_h2)
        # process_solve_puzzle(side_length, puzzle, back_track_hybrid)
        # process_solve_puzzle(side_length, puzzle, forward_check_std)
        # process_solve_puzzle(side_length, puzzle, forward_check_h1)
        # process_solve_puzzle(side_length, puzzle, forward_check_h2)

        print('Finish solve ', curr_puzzle)
        print()
        print()

    print("Finish solve all 3 puzzles, program end.")
