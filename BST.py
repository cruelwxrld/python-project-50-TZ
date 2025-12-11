class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        if not self.root:
            self.root = TreeNode(key, value)
            return

        node = self.root
        while node:
            if key < node.key:
                if not node.left:
                    node.left = TreeNode(key, value)
                    return
                node = node.left
            elif key > node.key:
                if not node.right:
                    node.right = TreeNode(key, value)
                    return
                node = node.right
            else:
                node.value = value
                return

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True if node.value is None else node.value
            node = node.left if key < node.key else node.right
        return None

    def delete(self, key):
        parent, node = None, self.root

        while node and node.key != key:
            parent = node
            node = node.left if key < node.key else node.right

        if not node:
            return

        if node.left and node.right:
            succ_parent, successor = node, node.right
            while successor.left:
                succ_parent, successor = successor, successor.left

            node.key, node.value = successor.key, successor.value
            parent, node = succ_parent, successor

        child = node.left or node.right

        if not parent:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child

    def height(self):
        stack = [(self.root, 1)] if self.root else []
        max_h = 0

        while stack:
            node, h = stack.pop()
            max_h = max(max_h, h)
            if node.left:
                stack.append((node.left, h + 1))
            if node.right:
                stack.append((node.right, h + 1))

        return max_h

    def is_balanced(self):
        stack = [(self.root, False, 0, 0)] if self.root else []
        heights = {}

        while stack:
            node, visited, left_h, right_h = stack.pop()

            if not node:
                continue

            if not visited:
                stack.append((node, True, 0, 0))
                stack.append((node.right, False, 0, 0))
                stack.append((node.left, False, 0, 0))
            else:
                if abs(left_h - right_h) > 1:
                    return False
                heights[node] = 1 + max(left_h, right_h)
                if stack and not stack[-1][1]:
                    if node == stack[-1][0].left:
                        stack[-1] = (stack[-1][0], False, heights[node], stack[-1][3])
                    else:
                        stack[-1] = (stack[-1][0], False, stack[-1][2], heights[node])

        return True

# Для проверки работоспособности методов - запустить BST.py

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10, "Root")
    bst.insert(5, "Left")
    bst.insert(15, "Right")
    bst.insert(3, "Left-Left")
    bst.insert(7, "Left-Right")

    print(f"Поиск:")
    print(f"Поиск 10: {bst.search(10)}")
    print(f"Поиск 5: {bst.search(5)}")
    print(f"Поиск 15: {bst.search(15)}")
    print(f"Поиск 3: {bst.search(3)}")
    print(f"Поиск 100: {bst.search(100)}\n")

    print(f"Высота: {bst.height()}")

    print(f"Сбалансировано: {bst.is_balanced()}")

    print("\nУдаление:")
    bst2 = BinarySearchTree()
    bst2.insert(10)
    bst2.insert(5)
    bst2.insert(15)
    bst2.insert(3)
    bst2.insert(7)

    result_before = bst2.search(5)
    print(f"До удаления 5: {result_before}")

    bst2.delete(5)
    print(f"После удаления 5: {bst2.search(5)}")

    print(f"Поиск 3 после удаления 5: {bst2.search(3)}")
    print(f"Поиск 7 после удаления 5: {bst2.search(7)}")
    print(f"Поиск 10 после удаления 5: {bst2.search(10)}")
    print(f"Поиск 15 после удаления 5: {bst2.search(15)}")

    print("\nУдаление корня:")
    bst3 = BinarySearchTree()
    bst3.insert(10)
    bst3.insert(5)
    bst3.insert(15)

    print(f"До удаления корня - Поиск 10: {bst3.search(10)}")
    print(f"До удаления корня - Поиск 5: {bst3.search(5)}")
    print(f"До удаления корня - Поиск 15: {bst3.search(15)}")

    bst3.delete(10)

    print(f"После удаления корня - Поиск 10: {bst3.search(10)}")
    print(f"После удаления корня - Поиск 5: {bst3.search(5)}")
    print(f"После удаления корня - Поиск 15: {bst3.search(15)}")

    print("\nНесбалансированное дерево:")
    bst4 = BinarySearchTree()
    for i in range(1, 6):
        bst4.insert(i)
    print(f"Высота: {bst4.height()}")
    print(f"Сбалансировано: {bst4.is_balanced()}")

    print("\nПустое дерево:")
    bst5 = BinarySearchTree()
    print(f"Высота: {bst5.height()}")
    print(f"Сбалансировано: {bst5.is_balanced()}")
    print(f"Поиск 10: {bst5.search(10)}")