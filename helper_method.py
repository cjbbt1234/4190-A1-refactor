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


def check_remain_domain(sol, block):
    result = True
    length = int(sol.get_size() / 2)
    un_sign_block = sol.get_count()
    for i in range(un_sign_block, length):
        domain_count = len(block[i])
        min_value = min(block[i])
        curr_block = block[i]
        if domain_count <= 2 and min_value+1 in curr_block:
            result = False
            break
        elif domain_count >= 5:
            continue
        else:
            if domain_count == 3:
                if (min_value + 1 in curr_block and (
                        min_value + length in curr_block or min_value + length + 1 in curr_block)):
                    result = False
                    break
                elif (min_value + length in block[i] and (
                        min_value + length - 1 in curr_block or min_value + length + 1 in curr_block)):
                    result = False
                    break
            elif domain_count == 4:
                if (
                        min_value + 1 in curr_block and min_value + length in curr_block and min_value + length + 1 in curr_block):
                    result = False
                    break
    return result
