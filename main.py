from draw import *
from star_list import *
import timeit
from read import *
import multiprocessing
from backtrack import back_track
from backtrack_heuristics import *
from forward_checking import forward_checking
from forward_checking_heuristics import *

WAIT_TIME = 10
LIMIT = 2


def back_track_std(solution, blocks, length):
    back_track.counter = 0
    back_track(solution, 0, blocks, length)
    return back_track.counter


def back_track_h1(solution, blocks, length):
    back_track_heuristic_one.counter = 0
    back_track_heuristic_one(solution, 0, blocks, length)
    return back_track_heuristic_one.counter


def back_track_h2(solution, blocks, length):
    back_track_heuristic_two.counter = 0
    back_track_heuristic_two(solution, 0, blocks, length)
    return back_track_heuristic_two.counter


def back_track_hybrid(solution, blocks, length):
    back_track_heuristic_hybrid.counter = 0
    back_track_heuristic_hybrid(solution, 0, blocks, length)
    return back_track_heuristic_hybrid.counter


def forward_check_std(solution, blocks, length):
    forward_checking.counter = 0
    forward_checking(solution, 0, blocks, length)
    return forward_checking.counter


def forward_check_h1(solution, blocks, length):
    forward_checking_heuristic_one.counter = 0
    forward_checking_heuristic_one(solution, 0, blocks, length)
    return forward_checking_heuristic_one.counter


def forward_check_h2(solution, blocks, length):
    forward_checking_heuristic_two.counter = 0
    forward_checking_heuristic_two(solution, 0, blocks, length)
    return forward_checking_heuristic_two.counter


def forward_check_hybrid(solution, blocks, length):
    forward_checking_heuristic_hybrid.counter = 0
    forward_checking_heuristic_hybrid(solution, 0, blocks, length)
    return forward_checking_heuristic_hybrid.counter


def solve_puzzle(length, blocks, fnc):
    solution = StarList(length * 2)
    start = timeit.default_timer()
    iteration = fnc(solution, blocks, length)
    stop = timeit.default_timer()
    print(fnc.__name__, ': Time cost: ', stop - start, 'second')
    print('Have ', iteration, 'iterations')
    print('Solution is:', solution.get_solution_list())
    print()
    print()
    draw_solution(blocks, solution.get_solution_list())
    return


def process_solve_puzzle(length, blocks, fnc):
    process = multiprocessing.Process(target=solve_puzzle, args=(length, blocks, fnc,))

    process.start()

    process.join(WAIT_TIME)

    if process.is_alive():
        print(fnc.__name__, " stucked ... let's kill it...No solution")
        print("Or it may because you keep the puzzle UI open for a long time and it reach the time limit...")
        print()
        print()
        process.kill()
        process.join()


if __name__ == '__main__':
    file_name_1 = "grid8x8.txt"
    file_name_2 = "grid10x10.txt"
    file_name_3 = "grid14x14.txt"

    puzzle = get_blocks(file_name_1)
    size = get_size(puzzle)
    side_length = get_length(size)

    process_solve_puzzle(side_length, puzzle, back_track_std)
    process_solve_puzzle(side_length, puzzle, back_track_h1)
    process_solve_puzzle(side_length, puzzle, back_track_h2)
    process_solve_puzzle(side_length, puzzle, back_track_hybrid)
    process_solve_puzzle(side_length, puzzle, forward_check_std)
    process_solve_puzzle(side_length, puzzle, forward_check_h1)
    process_solve_puzzle(side_length, puzzle, forward_check_h2)
    process_solve_puzzle(side_length, puzzle, forward_check_hybrid)
