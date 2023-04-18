from modules import AVL_Tree as Avl


avl_tree = Avl.AVLTree()
while True:
    print('''
Commands:
1 - insert
2 - find
3 - exit\n
    ''')
    print("Enter command:")
    try:
        cur_command = int(input())
        if cur_command == 1:
            print("Enter key to insert:")
            key_to_insert = int(input())
            avl_tree.insert(key_to_insert)
        if cur_command == 2:
            print("Enter key to find:")
            key_to_find = int(input())
            avl_tree.find(key_to_find)
        if cur_command == 3:
            print("Program finish")
            break
    except ValueError:
        print("Wrong command")
