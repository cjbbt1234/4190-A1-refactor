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
