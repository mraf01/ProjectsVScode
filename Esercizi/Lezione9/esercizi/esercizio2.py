'''
Data una lista di interi, chiamata tree, che rappresenta un albero binario, 
restituire True se l'albero è simmetrico; False altrimenti.

La lista di interi è formata così:

L'elemento in posizione 0 corrisponde alla radice
Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, 
significa che il nodo che corrisponde a quell'indice è una foglia.

Potete utilizzare la classe TreeNode per crearvi prima l'albero - anziché usare la lista tree - 
e poi visitare l'albero sfruttando gli oggetti di tipo TreeNode.

Test
print(symmetric([1,2,2,3,4,4,3]))  result: True
print(symmetric([1,2,2,None,3,None,3]))  result: False
print(symmetric([1,2,2,None,3,3,None]))  result: True
print(symmetric([1,2,2,3,None,None,3]))  result: True
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(tree, i):
    if i >= len(tree) or tree[i] is None:
        return None
    node = TreeNode(tree[i])
    node.left = build_tree(tree, 2 * i + 1)
    node.right = build_tree(tree, 2 * i + 2)
    return node

def is_mirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return (t1.val == t2.val and 
            is_mirror(t1.left, t2.right) and 
            is_mirror(t1.right, t2.left))

def symmetric(tree):
    if not tree:
        return True
    root = build_tree(tree, 0)
    return is_mirror(root.left, root.right)


# Test
print(symmetric([1,2,2,3,4,4,3]))  # True
print(symmetric([1,2,2,None,3,None,3]))  # False
print(symmetric([1,2,2,None,3,3,None]))  # True
print(symmetric([1,2,2,3,None,None,3]))  # True