from graph import Graph


class Alphabet:
    def __init__(self):
        """
        Letters - set of letters encountered so far
        Relations - graph of relations between letters
        """

        self.letters = set()
        self.relations = Graph()

    def _compare_words(self, next_word, prev_word):
        """
        Comparing words in pairs in order to find the differing letters and add them to the graph
        :param string next_word:
        :param string prev_word:
        :return:
        """

        if len(prev_word) == 0:
            for letter in next_word:
                self.relations.add_to_graph(None, letter)
            return

        for p, n in zip(prev_word, next_word):
            if p != n:
                self.relations.add_to_graph(p, n)
                break

    def get_alphabet(self, unknown_dictionary):
        """
        We get an unknown dictionary, insert letters from it to relations graph
        and perform topological sort over the letters
        :param iterable unknown_dictionary: dictionary with unknown lexicographical order
        :return list: sorted list of letters from dictionary
        """

        prev_word = ''

        for word in unknown_dictionary:
            self._compare_words(word, prev_word)
            prev_word = word

        return self.relations.start_topological_sort()
