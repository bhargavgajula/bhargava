from random import randint
x=randint(1,100)
y=randint(1,100)
z=randint(1,100)
w=randint(1,100)
p=randint(1,100)
q=randint(1,100)
r=randint(1,100)

class Bts:
    def __init__(self,Node):
        self.left=None
        self.right=None
        self.val=Node
def insert(root):
    if(root!=Node):
        print("Node is empty")
    elif(Node==root):
         print(str(root.val),end="->")
    elif(Node<root):
        print(root.left)
    else:
        print(root.right)
        return root
root=Bts(x)
root.left=Bts(y)
root.right=Bts(z)
root.left.left=Bts(w)
root.left.right=Bts(p)
root.right.left=Bts(q)
root.right.right=Bts(r)