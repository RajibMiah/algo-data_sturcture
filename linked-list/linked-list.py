

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self , data ):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next    
        itr.next = Node(data, None)
        

    def insert_values(self , data_list):
        self.head = None 
        for data in data_list :
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None :
           self.insert_at_begining(data_to_insert)
           return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert , itr.next)
                itr.next = node
                break

            itr = itr.next   


    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next

        return counter    

    def print(self):
        if self.head is None:
            print('Linked list is empty')
        itr = self.head
        count = 0
        lltr = ''
        while itr :
            if count == self.get_length() - 1:
                lltr += str(itr.data) + '--> null'
            else:
                lltr += str(itr.data) + '-->'      
            count += 1  
            itr = itr.next
        print(lltr)

    def remove_by_value(self, value):
        itr = self.head
        while itr :
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next

    def remove_at(self , index):
        if index < 0 or index>self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head 
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next 
            count += 1       

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        count =  0
        itr = self.head
    
        while itr:
            if index == count - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next   



if __name__ == "__main__":
    ll = LinkList()
    ll.insert_values(["banana" , "mango" , "grapes" , "Orange" , "rice"])
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(50)
    # ll.insert_at_begining(89)
    # ll.print()
    # ll.insert_at_end(10)
    # ll.insert_at_end(30)
    ll.print()
    print("length:: " , ll.get_length())
    ll.print()
    print("length:: " , ll.get_length())
    ll.insert_at("begun", 3)
    ll.print()
    print("length:: " , ll.get_length())
    ll.insert_after_value("rice","apple") 
    ll.print()
    print("length:: " , ll.get_length())
    ll.remove_by_value("mango") # remove orange from linked list
    ll.print()
    print("length:: " , ll.get_length())

   