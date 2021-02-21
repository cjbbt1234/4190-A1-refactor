from tkinter import *

COLORS = ['floral white', 'brown1', 'LightCyan3', 'indian red', 'SlateBlue3', 'wheat4', 'dark turquoise',
          'LightGoldenrod2',
          'tan2', 'RoyalBlue4', 'tomato3', 'LightYellow3', 'gray57', 'khaki4', 'gray53', 'orange red']


def draw_solution(blocks, solution):
    """This function draw the star battle in a window

    :param blocks: Blocks that describes the star battle puzzle
    :param solution: A list that contains the solution of star battle
    :return: No return
    """

    window = Tk()
    window.title("Star Battle")
    star = '\u2605'
    window.geometry('1280x720')
    for index in range(len(blocks)):
        block = blocks[index]
        for p in block:
            row = int((p - 1) / len(blocks))
            col = int((p - 1) % len(blocks))
            if p in solution:  # if this position is in solution list, then we need to draw star in it
                Label(window, bg=COLORS[index], relief=GROOVE, width=5, height=3, text=star).grid(row, col)
            else:
                Label(window, bg=COLORS[index], relief=GROOVE, width=5, height=3).grid(row, col)
    window.mainloop()
