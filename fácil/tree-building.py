class Tree():
    def __init__(self):
        self.root = {
            'properties': {'id': 0, 'parent_id': 0},
        }

    def add_node(self, node_id, parent_id = 0):

        def find_parent_node(current_node:dict) -> dict:
            if current_node['properties']['id'] == parent_id:
                return current_node

            if len(current_node) > 1:
                for i in range(1, len(current_node)):
                    parent_node = find_parent_node(current_node[i])
                    if isinstance(parent_node, dict):
                        return parent_node


        parent_node = find_parent_node(self.root)

        parent_node[len(parent_node)] = {'properties': {'id': node_id, 'parent_id': parent_id},}



def tests():
    """
        root (ID: 0, parent ID: 0)
        |-- child1 (ID: 1, parent ID: 0)
        |
        +-- child2 (ID: 3, parent ID: 0)
        |    +-- grandchild3 (ID: 6, parent ID: 3)
        +-- child3 (ID: 5, parent ID: 0)

    """
    root = {
        'properties': {'id': 0, 'parent_id': 0},
        1: {
            'properties': {'id': 1, 'parent_id': 0},
            1: {
                'properties': {'id': 2, 'parent_id': 1}
            }
        }
    }
    """
    [[0, 0], []]
    
    """
    print(list(root))
    print(len(root))

# tests()

if __name__ == '__main__':
    tree = Tree()
    print(tree.root)
    tree.add_node(1, 0)
    print(tree.root)
    tree.add_node(2, 1)
    print(tree.root)
    tree.add_node(3, 0)
    print(tree.root)
    tree.add_node(4, 2)
    print(tree.root)