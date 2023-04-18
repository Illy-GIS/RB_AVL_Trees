from modules import RB_Tree as Rb


if __name__ == "__main__":
    rb_tree = Rb.RedBlackTree()
    rb_tree.insert(70)
    rb_tree.insert(60)
    rb_tree.insert(85)
    rb_tree.insert(80)
    rb_tree.insert(95)
    rb_tree.insert(65)
    while True:
        print('''
Instructions:
Enter 1 to insert key
Enter 2 to find key
Enter 3 to delete key
Enter 4 to exit program
Enter 5 to delete in range
        ''')
        print("Enter the instruction:")
        try:
            instruction = int(input())
            if instruction == 1:
                print("Enter key you want to insert:")
                key_to_insert = int(input())
                rb_tree.insert(key_to_insert)
            if instruction == 2:
                print("Enter key you want to find:")
                key_to_find = int(input())
                rb_tree.find(key_to_find)
                rb_tree.print_tree()
            if instruction == 3:
                print("Enter key you want to delete:")
                key_to_delete = int(input())
                rb_tree.delete_node(key_to_delete)
            if instruction == 4:
                break
            if instruction == 5:
                print("Enter min to delete:")
                min_delete = int(input())
                print("Enter max to delete:")
                max_delete = int(input())
                for i in range(max_delete - min_delete + 1):
                    rb_tree.delete_node(min_delete)
                    min_delete += 1
        except ValueError:
            print("Entered instruction or value is wrong!")
