# Implement an algorithm to find the kth to last element of a singly linked list
# Magdalena Grodzińska

# linked list implementation

class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self):
        self.data = new_data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


# main function

def find_kth(list, k):
    if list == None:
        return None

    length = count_elements(list)

    if k >= length:
        return None;

    how_many_to_go = length - k
    return iterate_n_elements(list, how_many_to_go)


# helper functions

def count_elements(list):
    counter = 0
    node_i = list

    while node_i != None:
        counter += 1
        node_i = node_i.get_next()

    return counter


def iterate_n_elements(list, n):
    counter = 0
    node_i = list
    element = None

    while counter < n:
        element = node_i.get_data()
        #print(str(counter) + " " + str(element))
        node_i = node_i.get_next()
        counter += 1

    return element


# testing functions

def build_sample_list(n):
    if n == 0:
        return None

    list = Node(0, None)
    list_i = list

    for i in range(n - 1):
        new_node = Node(i+1, None)
        list_i.set_next(new_node)
        list_i = list_i.get_next()

    return list


def test(k, list_length):
    sample_list = build_sample_list(list_length)
    result = find_kth(sample_list, k)

    print(result)
    return result

res = test(2, 1)
assert(res == None)
res = test(0, 1)
assert(res == 0)
res = test(0, 0)
assert(res == None)
res = test(1, 1)
assert(res == None)
res = test(9, 10)
assert(res == 0)
res = test(0, 10)
assert(res == 9)
