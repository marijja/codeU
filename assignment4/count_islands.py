class CountIslands():
    def __init__(self):
        self._clear_data()

    def _clear_data(self):
        """*_row_islands is a list of sets containing tile numbers that belong to some island in the previous row
        """
        self.prev_row_islands = []
        self.new_row_islands = []
        self.counter = 0

    def _create_island(self, tile_num):
        """We either create new set (new island) or extend an existing one.
        :param tile_num:
        :return:
        """
        added = False
        if not self.new_row_islands:
            self.new_row_islands.append({tile_num})
            return

        for island in self.new_row_islands:
            if tile_num - 1 in island:
                island |= {tile_num}
                added = True

        if not added:
            self.new_row_islands.append({tile_num})

    def _compare_rows(self):
        """We traverse two lists of sets to check how many sets in second list (self.new_row_islands)
        do not intersect with any of the sets from list one (self.prev_row_islands).
        We do it so that the complexity is O(n), incrementing one iterator or another, until we check
        all the sets from list two.
        :return:
        """
        if not self.prev_row_islands and self.new_row_islands:
            self.counter += len(self.new_row_islands)
            return
        if not self.new_row_islands:
            return

        prev_row_i = 0
        new_row_i = 0
        island_is_new = True
        max_prev = len(self.prev_row_islands)

        while new_row_i < len(self.new_row_islands):
            new_island = self.new_row_islands[new_row_i]
            prev_island = self.prev_row_islands[prev_row_i]

            if not new_island.isdisjoint(prev_island):
                if not island_is_new: # We delete some excessive islands from previous row (see: testWeirdCase in tests)
                    self.counter -= 1
                island_is_new = False
                if max(prev_island) < max(new_island) and prev_row_i < max_prev - 1:
                    prev_row_i += 1
                else:
                    island_is_new = True
                    new_row_i += 1
            elif min(prev_island) > max(new_island) or max(prev_island) >= max_prev - 1:
                if island_is_new:
                    self.counter += 1
                island_is_new = True
                new_row_i += 1
            elif prev_row_i < max_prev - 1:
                prev_row_i += 1

    def count(self, map):
        """Dynamic approach - traverse the matrix row by row
        Create lists of sets that indicate continuous islands in a given row
        Create them for two subsequent rows and compare to count new islands

        Complexity: O(n) where n is number of tiles in map
        (we traverse each row 3 times)
        :param map:
        :return:
        """
        self._clear_data()

        for row in map:
            for tile_num in range(len(row)):
                if row[tile_num]:
                    self._create_island(tile_num)

            self._compare_rows()
            self.prev_row_islands = list(self.new_row_islands)
            self.new_row_islands.clear()

        return self.counter
