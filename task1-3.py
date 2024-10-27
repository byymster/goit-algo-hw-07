class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для вставки значення у двійкове дерево пошуку
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Функція для знаходження найбільшого значення у двійковому дереві пошуку
def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.value

# Функція для знаходження найменшого значення у двійковому дереві пошуку
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.value

# Функція для знаходження суми всіх значень у двійковому дереві пошуку
def find_sum(root):
    if root is None:
        return 0
    return root.value + find_sum(root.left) + find_sum(root.right)

# Приклад використання
root = TreeNode(20)
insert(root, 10)
insert(root, 30)
insert(root, 25)
insert(root, 35)

print("Найбільше значення у дереві:", find_max(root))
print("Найменше значення у дереві:", find_min(root))
print("Сума всіх значень у дереві:", find_sum(root))
