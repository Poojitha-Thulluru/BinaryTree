# trees can grow from top to bottom - have a direction downwards
# root node = node which does not have any parent
# nodes = elements in a tree
# immediate predecessor of any node is its parent - root doesn't have parent node
# immediate successor of any node is its children - leaf nodes doesn't have children
# leaf nodes = external nodes
# non-leaf nodes(at-least 1 child) = internal nodes
# Ancestors of a node = any predecessor(1 or many) on the path from root to that node
# Descendant of a node = any successor node on the path from that node to the leaf node
# degree of a node = number of children of a node
# depth = no. of edges from root to the node
# height = no. of edges from the node to its deepest(longest path) leaf node
# if n nodes , then n-1 edges will be present

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def create(self):
        data = int(input("Enter data (-1 for no node) : "))
        if data == -1:
            return
        new_node = Node(data)
        print(f"Enter left child of {data}")
        new_node.left = self.create()
        print(f"Enter right child of {data}")
        new_node.right = self.create()

        return new_node

    def pre_order_traversal(self, root):
        if root is None:
            return
        print(root.data)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)


if __name__ == "__main__":
    binary_tree = Tree()
    print("Welcome!!!")
    root = None
    while True:
        print("\n1 - Create")
        print("2 - display in pre-order")
        print("3 - exit")
        print("Enter your choice between (1-3) : ")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            root = binary_tree.create()
            print("The tree is created successfully")
        elif choice == 2:
            print("The pre-order traversal is : ")
            binary_tree.pre_order_traversal(root)
        elif choice == 3:
            print("Exiting....")
            break
        else:
            print("Invalid choice")



