from star import Star


class StarList:
    """
    Class for star list, has three field, a list contain stars, the list size, the count of assignment stars.
    """
    def __init__(self, size):
        self.list = []
        self.size = size
        for i in range(size):
            self.list.append(Star())
        self.count = 0

    def __str__(self):
        a = []
        for i in self.list:
            a.append('(' + str(i) + ')')
        return str(a)

    def get_solution_list(self):
        """
        Get all star position in puzzle

        :param self A Star_list
        :return: A array
        """
        result = []
        for s in self.list:
            result.append(s.get_position())
        return result

    def set_star(self, index, p, b):
        """
        Set a new star to the Star_list

        :param index: the index of star in the Star_list
        :param p: the star position in the puzzle
        :param b: the block it belongs to
        :return: no return
        """
        temp = self.list[index]
        temp.set_position(p)
        temp.set_block(b)
        self.count = self.count + 1

    def reset_star(self, index):
        """
        Reset a assignment of a Star in Star_list

        :param index: the Star index in the Star_list
        :return: no return
        """
        temp = self.list[index]
        temp.set_block(-1)
        temp.set_position(-1)
        self.count = self.count - 1

    def get_star(self, index):
        return self.list[index]

    def get_size(self):
        return self.size

    def get_count(self):
        return self.count

    def neighbor_check(self):
        """
        Check if current assignment stars in star list is consist with neighbor constrain
        :return: Boolean
        """
        length = self.size / 2
        for i in range(self.count):
            star_a_position = self.list[i].get_position()
            for j in range(i, self.count):
                star_b_position = self.list[j].get_position()
                (x1, y1) = (int((star_a_position - 1) / length), (star_a_position - 1) % length)
                (x2, y2) = (int((star_b_position - 1) / length), (star_b_position - 1) % length)
                if abs(x1 - x2) + abs(y1 - y2) == 1 or (abs(x1 - x2) == 1 and abs(y1 - y2) == 1):
                    return False
        return True

    def block_check(self, limit):
        """
        Check if current assignment stars in star list is consist with block constrain
        :param limit: the number stars each block, row, column must contain
        :return: Boolean
        """
        result = True
        size = int(len(self.list) / limit)
        counter = [0 for i in range(size)]
        for i in self.list[0:self.count]:
            counter[i.get_block() - 1] = counter[i.get_block() - 1] + 1
            if counter[i.get_block() - 1] > limit:
                result = False
                break
        return result

    def row_check(self, limit):
        """
        Check if current assignment stars in star list is consist with row constrain
        :param limit: the number stars each block, row, column must contain
        :return: Boolean
        """
        result = True
        size = int(len(self.list) / limit)
        counter = [0 for i in range(size)]
        for i in self.list[0:self.count]:
            curr_star_position = i.get_position()
            counter[int((curr_star_position - 1) / size)] = counter[int((curr_star_position - 1) / size)] + 1
            if counter[int((curr_star_position - 1) / size)] > limit:
                result = False
                break
        for i in counter:
            if i > limit:
                result = False
                break
        return result

    def col_check(self, limit):
        """
        Check if current assignment stars in star list is consist with column constrain
        :param limit: the number stars each block, row, column must contain
        :return: Boolean
        """
        result = True
        size = int(len(self.list) / limit)
        counter = [0 for i in range(size)]
        for i in self.list[0:self.count]:
            curr_star_position = i.get_position()
            counter[(curr_star_position - 1) % size] = counter[(curr_star_position - 1) % size] + 1
            if counter[(curr_star_position - 1) % size] > limit:
                result = False
                break
        for i in counter:
            if i > limit:
                result = False
                break
        return result

    def is_consistent(self, limit):
        """
        Check if current assignment stars in star list is consist with all constrains
        :param limit: the number stars each block, row, column must contain
        :return: Boolean
        """
        return self.neighbor_check() and self.block_check(limit) and self.col_check(
            limit) and self.row_check(limit)
