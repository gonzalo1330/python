# main class
import tree

# build tree below as the example
#     5
#    /  \
#   2    6
#  / \    \
# 1   4    7
#     /
#    3

root = tree.Node(5)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(4)
root.insert(3)
root.insert(7)

# iterator testing
iterator = tree.BinaryTreeIterator(root)
print(iterator.hasNext())

while(iterator.hasNext()):
  iterator.next()

print(iterator.hasNext()) # verified once empty tree, we no longer have a hasNext


# handling error cases
try:
  iterator.next()
except Exception as error:
  print('Error:', error)

print('Binary Tree iterator completed')