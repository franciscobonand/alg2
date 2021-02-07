class CTrie:
    def __init__(self, value='', has_data=False, numeric_value=None, parent=None):
        self.value = value
        self.has_data = has_data
        self.numeric_value = numeric_value
        self.parent = parent
        self.children = {}

    # add_node adds a new node to the ctrie as one of the current node's children
    def add_node(self, key, node):
        if node == None:
            node = CTrie()

        node.parent = self
        node.value = key
        self.children[key] = node

    # add inserts a new word into de ctrie, whether creating a new node or updating the ctrie structure in case
    # the new word shares a common prefix with another word inside the ctrie
    def add(self, word, value):
        common_index, key = self.return_prefix(word)

        # case where there isn't a node with given word prefix in the ctrie
        if key == None:
            self.add_node(word, CTrie(has_data=True, numeric_value=value))
            
            # turns current node into an internal node (which doesn't contain data besides it's children)
            if self.has_data and self.numeric_value != 0:
                self.add_node('', CTrie(has_data=True, numeric_value=self.numeric_value))
                self.has_data = False
                self.numeric_value = None

        # case where the new word has an already existing key as it's prefix (e.g.: word=banana / key=ban)
        elif common_index == len(key):
            self.children[key].add(word[common_index:], value)

        # case where the new word shares a common prefix with a key (e.g.: word=casa / key=camelo)
        else:
            common_prefix = word[:common_index]
            aux_node = self.children.pop(key)
            aux_node.value = key[common_index:]

            self.add_node(common_prefix, None)
            self.children[common_prefix].add_node(word[common_index:], CTrie(has_data=True, numeric_value=value))
            self.children[common_prefix].add_node(key[common_index:], aux_node)

    # return_prefix returns the biggest common prefix that exists in ctrie's nodes.
    # returns None in case a common prefix isn't found
    def return_prefix(self, word):
        for key in self.children.keys():
            for i in range(len(key), 0, -1):
                if key[:i] == word[:i]:
                    return (i, key)

        return (-1, None)

    # contains recursively searches for a word (the entire word or it's separated suffixes) and returns
    # that word's current numeric value. If the word is not found, returns -1
    def contains(self, word):
        if word == self.value and self.numeric_value != None:
            return self.numeric_value

        common_index, key = self.return_prefix(word)

        if key == None:
            return -1

        return self.children[key].contains(word[common_index:])