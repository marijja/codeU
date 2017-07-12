from graph import Graph


class Alphabet:
    def __init__(self):
        self.letters = set()
        self.relations = Graph()

    def _compare_words(self, next_word, prev_word):
        if len(prev_word) == 0:
            return

        for i in range(min(len(next_word), len(prev_word))):
            p = prev_word[i]
            n = next_word[i]

            if p != n:
                if n not in self.letters:
                    self.letters.add(n)
                self.relations.add(p, n)

    def get_alphabet(self, unknown_dictionary):
        prev_word = ''

        for word in unknown_dictionary:
            self._compare_words(word, prev_word)
            prev_word = word

        return self.relations.start_topological_sort()
