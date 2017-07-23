from order import Order


class Sorter:
    def __init__(self, permutation, sorted_sequence):
        """
        Order is a class implementing comparison and min in our ordering.
        :param list(int) self.permutation: Initial self.permutation to sort
        :param list(int) sorted_sequence: Order we want to achieve with self.permutation
        """
        self.N = len(sorted_sequence)
        self.order = Order(sorted_sequence)
        self.sorted_sequence = sorted_sequence
        self.permutation = permutation

    def _swap_values(self, min_value_i, value_i):
        """
        Swapping value with min value using 0 as buffer
        :param int min_value_i: Index of min value to swap
        :param int value_i: Index of value to swap
        """
        if min_value_i == value_i:
            return

        zero_i = self.permutation.index(0)

        if value_i != zero_i:  # we don't need to swap 0 with 0
            self.permutation[value_i], self.permutation[zero_i] = self.permutation[zero_i], self.permutation[value_i]
            print(self.permutation)
            value_i, zero_i = zero_i, value_i

        self.permutation[min_value_i], self.permutation[zero_i] = self.permutation[zero_i], self.permutation[min_value_i]
        print(self.permutation)

    def _move_zero(self):
        """
        Moving zero right or left until it is sorted to its proper position
        """
        if 0 not in self.permutation:
            return self.permutation

        zero_i = self.permutation.index(0)

        while zero_i < self.N - 1 and self.order.less_than(self.permutation[zero_i + 1], self.permutation[zero_i]):
            self.permutation[zero_i], self.permutation[zero_i + 1] = self.permutation[zero_i + 1], self.permutation[zero_i]
            zero_i += 1
            print(self.permutation)

        while zero_i > 0 and self.order.less_than(self.permutation[zero_i], self.permutation[zero_i - 1]):
            self.permutation[zero_i], self.permutation[zero_i - 1] = self.permutation[zero_i - 1], self.permutation[zero_i]
            zero_i -= 1
            print(self.permutation)

        return self.permutation

    def sort(self):
        """
        The problem is actually sorting with memory O(1) and an artificial order of elements.
        We use the selection sort, because we don't need to manage the recursive calls in it.

        We sort using zero as a buffer and then insert it to its proper place in permutation.
        :return list(int): Permutation after ordering
        """
        print(self.permutation)
        if not self.permutation or self.permutation == self.sorted_sequence:
            return self.permutation

        for i in range(self.N):
            min_value = self.order.min_omit_zero(self.permutation[i:self.N])
            min_index = self.permutation.index(min_value)
            self._swap_values(min_index, i)

        return self._move_zero()
