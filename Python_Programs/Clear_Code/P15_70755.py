with open('P15_tree.txt', 'w') as file:
    tree_str = '''   X
     XXX
    XXXXX
      X
      X
      X'''
    file.write(tree_str)
print(file.read())