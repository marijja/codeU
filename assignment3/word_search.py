class Word_searcher():
    def __init__(self, rows, columns, matrix, words):
        self.words = words
        self.rows = rows
        self.columns = columns
        self.matrix = matrix
        self.starting_points = {}
        self.found_words = []

    def _check_neighbours(self, x, y, letter):
        res = []

        for i in range(-1, 2):
            if self.columns > x + i >= 0:
                for j in range (-1, 2):
                    if self.rows > y + j >= 0:
                        n_x = x + i
                        n_y = y + j

                        if self.matrix[n_x][n_y] == letter:
                            res.append({ 'x': n_x, 'y': n_y })

        return res

    def _find_first_letter(self, letter):
        res = []

        for y in self.rows:
            for x in self.columns:
                if self.matrix[x][y] == letter:
                    res.append({'x': x, 'y': y})

        return res

    def _find_next_letter(self, word, current_x, current_y, current_pos):
        if current_pos == len(word):
            return True
        else:
            neighbours = self._check_neighbours(current_x, current_y, word[current_pos])
            current_pos += 1

            for n in neighbours:
                if self._find_next_letter(word, n.x, n.y, current_pos):
                    return True

            return False

    def find_words(self):
        for word in self.words:
            if word[0] not in self.starting_points:
                self.starting_points.update({word[0] : self._find_first_letter(word[0])})

        for word in self.words:
            for start_position in self.starting_points[word[0]]:
                if self._find_next_letter(word, start_position.x, start_position.y, 0):
                    self.found_words.append(word)
                    break

        return set(self.found_words)

def word_searcher(rows, columns, matrix, words):
    word_helper = Word_searcher(rows, columns, matrix, words)
    return word_helper.find_words()