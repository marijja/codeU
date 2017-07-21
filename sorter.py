class Order:
    def __init__(self, sorted_sequence):
        self.N = len(sorted_sequence)
        self.relations = self._set_order(sorted_sequence)

    def _set_order(self, sorted_sequence):
        """
        We determine the order of elements so that we can sort them.
        :param sorted_sequence: list determining the order of elements
        :return:
        """
        new_order = set()
        for i in range(self.N - 1):
            new_order.add((sorted_sequence[i], sorted_sequence[i + 1]))
        return new_order

    def compare(self, value1, value2):
        pass

    def get_min(self, iterable):
        pass



class Sorter:
    def __init__(self, permutation, sorted_sequence):
        """
        Order is a set of pairs (tuples with 2 elemtents) that determine the ordering that we want to acheive
        """
        self.N = len(sorted_sequence)
        self.order = Order(sorted_sequence)
        self.permutation = permutation

    def _print_permutation(self, permutation, empty_slot):
        permutation.insert(empty_slot, 0)
        print(permutation)
        permutation.remove(0)

    def _move_to_empty_slot(self, empty_slot_i, number_i, permutation):
        value = permutation[number_i]
        empty_slot_i, number_i = number_i, empty_slot_i
        permutation.remove(value)
        permutation.insert(number_i, value)
        self._print_permutation(permutation, empty_slot_i)

        return empty_slot_i, number_i

    def _insert_zero(self, zero_position, permutation):
        permutation.insert(zero_position, 0)
        i = zero_position

        while i < self.N - 1 and permutation[i] > permutation[i + 1]:
            permutation[i], permutation[i + 1] = permutation[i + 1], permutation[i]
            i += 1
            print(permutation)

        while i > 0 and permutation[i] < permutation[i - 1]:
            permutation[i], permutation[i - 1] = permutation[i - 1], permutation[i]
            i -= 1
            print(permutation)

        return permutation

    def _remove_zero(self):
        empty_slot = self.permutation.index(0)
        current_permutation = list(self.permutation)
        current_permutation.remove(0)

        return empty_slot, current_permutation

    def sort(self):
        """
        The problem is actually sorting with memory O(1) and given order of elements.
        We use the selection sort, because we don't need to manage the recursive calls in it.

        We remove the 0 from permutation, sort using it as a buffer and then insert it to the permutation.
        :return:
        """

        print(self.permutation)
        empty_slot, current_permutation = self._remove_zero()

        for i in range(self.N):
            try:
                min_value = min(current_permutation[i:self.N]) # min should be in our ordering - override operators?
                min_index = current_permutation.index(min_value)
                if min_index == i:
                    continue
                print(f"p {current_permutation} min {min_index} i {i}")
            except ValueError:
                break
            else:
                future_min_position, new_i_position = self._move_to_empty_slot(empty_slot, i, current_permutation)
                empty_slot, new_min_position = self._move_to_empty_slot(future_min_position, min_index, current_permutation)

        return self._insert_zero(empty_slot, current_permutation)
