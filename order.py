class Order:
    def __init__(self, sorted_sequence):
        self.sorted_sequence = sorted_sequence
        self.N = len(self.sorted_sequence)
        self.indexes = {n : self.sorted_sequence.index(n) for n in sorted_sequence}

    def less_than(self, value1, value2):
        return self.indexes[value1] < self.indexes[value2]

    def min_omit_zero(self, iterable):
        """
        :param list(int) iterable: Subarray of sorted_sequence
        :return int: Min value from subarray
        """
        if not iterable or not set(iterable).issubset(set(self.sorted_sequence)):
            raise ValueError

        min_i = self.N - 1
        min_val = self.sorted_sequence[min_i]
        for value in iterable:
            min_val = value if value != 0 and self.indexes[value] < min_i else min_val
            min_i = self.indexes[min_val]
        return min_val