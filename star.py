class Star:
    """
    Class for stars, has two field, star position in the puzzle, and the block it belongs to.
    """
    def __init__(self):
        self.position = -1
        self.block = -1

    def set_position(self, p):
        self.position = p

    def get_position(self):
        return self.position

    def set_block(self, b):
        self.block = b

    def get_block(self):
        return self.block

    def __str__(self):
        return str(self.position) + '+' + str(self.block)
