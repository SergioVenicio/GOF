from collections.abc import Iterator


class Words(Iterator):
    def __init__(self, collection=[], reverse=False):
        self._collection = list(collection)
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def add_word(self, word):
        self._collection.append(word)

    def __next__(self):
        try:
            word = self._collection[self._position]
        except IndexError:
            raise StopIteration()

        self._position += -1 if self._reverse else 1
        return word

if __name__ == '__main__':
    text = Words()
    text.add_word('Test 1')
    text.add_word('Test 2')
    text.add_word('Test 3')
    text.add_word('Test 4')

    print('\n'.join(text))
    print('***')

    reverse_text = Words(reverse=True)
    reverse_text.add_word('Test 1')
    reverse_text.add_word('Test 2')
    reverse_text.add_word('Test 3')
    reverse_text.add_word('Test 4')

    print('\n'.join(reverse_text))