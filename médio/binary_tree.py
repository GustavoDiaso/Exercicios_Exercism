class BinaryTree():
    def __init__(self, root):
        if type(root) == float or type(root) == int:
            self.structure = [root, [], []]
        else:
            raise ValueError('the root value must be a number')


    def add_node(self, node):
        if type(node) == float or type(node) == int:

            # comece sempre passando a raiz para a função vista_nó
            def visit_node(n):

                if n[0] >= node:
                    # verfica se à esquerda do nó está vazio
                    if len(n[1]) == 0:
                        n[1] = [node, [], []]
                    else:
                        visit_node(n[1])
                        
                else:
                    # verfica se à direita do nó está vazio
                    if len(n[2]) == 0:
                        n[2] = [node, [], []]
                    else:
                        visit_node(n[2])


            visit_node(self.structure)

            return self.structure

        else:
            raise ValueError('the node value must be a number')


arvore_binaria = BinaryTree(4)
print(arvore_binaria.add_node(2))
print(arvore_binaria.add_node(6))
print(arvore_binaria.add_node(3))
print(arvore_binaria.add_node(1))
print(arvore_binaria.add_node(5))
print(arvore_binaria.add_node(7))



