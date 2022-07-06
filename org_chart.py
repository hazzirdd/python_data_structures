from hashlib import new


class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree():
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)

    def total_nodes(self):
        
        def num_children(node, total):
            inner_nodes = total

            for child in node.children:
                inner_nodes += 1
                inner_nodes = num_children(child, inner_nodes)

            return inner_nodes

        return num_children(self.root, 0)


name = 'Bob'
my_reports = ['Alpha', 'Bravo', 'Charlie']

def make_tree(ceo, reports):
    new_tree = Node(ceo, reports)
    return Tree(new_tree)

tree = make_tree(name, my_reports)
print(tree.total_nodes())
