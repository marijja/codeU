from order import Order


class Sorter:
    def __init__(self, permutation, sorted_sequence):
        """
        Order is a class implementing comparison and min in our ordering.
        :param list(int) permutation: Initial permutation to sort
        :param list(int) sorted_sequence: Order we want to achieve with permutation
        """
        self.N = len(sorted_sequence)
        self.order = Order(sorted_sequence)
        self.initial_permutation = permutation
        self.sorted_sequence = sorted_sequence

    def _swap_values(self, x_i, y_i, permutation):
        """
        Swapping values using 0 as buffer
        :param int x_i: Index of first value to swap
        :param int y_i: Index of second value to swap
        :param list(int) permutation: Permutation that we process
        :return: Permutation after values swapping
        """

        zero_i = permutation.index(0)
        if y_i != zero_i:  # we don't need to swap 0 with 0
            permutation[y_i], permutation[zero_i] = permutation[zero_i], permutation[y_i]
            print(permutation)
            y_i, zero_i = zero_i, y_i

        permutation[x_i], permutation[zero_i] = permutation[zero_i], permutation[x_i]
        print(permutation)

        return permutation

    def _move_zero(self, permutation):
        """
        :param list(int) permutation: Permutation where zero might not be sorted
        :return list(int): Permutation after zero is sorted to proper position
        """
        if 0 not in permutation:
            return permutation

        zero_i = permutation.index(0)

        while zero_i < self.N - 1 and self.order.less_than(permutation[zero_i + 1], permutation[zero_i]):
            permutation[zero_i], permutation[zero_i + 1] = permutation[zero_i + 1], permutation[zero_i]
            zero_i += 1
            print(permutation)

        while zero_i > 0 and self.order.less_than(permutation[zero_i], permutation[zero_i - 1]):
            permutation[zero_i], permutation[zero_i - 1] = permutation[zero_i - 1], permutation[zero_i]
            zero_i -= 1
            print(permutation)

        return permutation

    def sort(self):
        """
        The problem is actually sorting with memory O(1) and an artificial order of elements.
        We use the selection sort, because we don't need to manage the recursive calls in it.

        We sort using zero as a buffer and then insert it to its proper place in permutation.
        :return list(int): Permutation after ordering
        """
        print(self.initial_permutation)
        if not self.initial_permutation or self.initial_permutation == self.sorted_sequence:
            return self.initial_permutation

        permutation = self.initial_permutation

        for i in range(self.N):
            min_value = self.order.min_omit_zero(permutation[i:self.N])
            min_index = permutation.index(min_value)
            if min_index != i:
                permutation = self._swap_values(min_index, i, permutation)

        return self._move_zero(permutation)
