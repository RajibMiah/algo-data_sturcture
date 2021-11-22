
class Binary_serach_tree_node():

    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self ,data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)    
            else:
                self.left = Binary_serach_tree_node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_serach_tree_node(data)    

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
            
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.find_min()                

       
    def in_order_traversal(self):
        elements  = []

        # traverse end of the left subtree 
        if self.left:
          # elements += self.left.in_order_traversal 
          # referse that the return element  arrray  from the stack is add to source  element   
          elements += self.left.in_order_traversal()

        # retrive the value from the end of the node source  . Of last coroutine schudule  
        elements.append(self.data)

        if self.right:
            # elements += self.left.in_order_traversal 
            # referse that the return element  arrray  from the stack is add to source  element   
           elements += self.right.in_order_traversal()
        
        return elements    

    def search(self, value):

        if self.data == value:
            # print('data' , value)
            return True

        if  value < self.data  :
            if self.left:
                return self.left.search(value)
            else:
                return False             
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

def build_tree(elements):
    root = Binary_serach_tree_node(elements[0])

    for i in range(1 ,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17 , 4 , 1, 20 ,9,23,18,34  , 18 ,4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))
