class TreeNode:

    def __init__(self, name , designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add_child(self , child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self , propertry_name ):
 
        if propertry_name == 'name':
            value = self.name
        elif propertry_name == 'designation':
            value = self.designation
        elif propertry_name == 'both':
            value = self.name + "("+ self.designation + ")"        

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print( prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(propertry_name)

def build_product_tree():

    CEO = TreeNode("Nilupul" , "CEO")

    CTO = TreeNode("Chinmay" , "CTO")
    
    infra_head = TreeNode('Vishwa' , "Infrastructure Head")
    infra_head.add_child(TreeNode('Dhaval' , "Cloud Manager"))
    infra_head.add_child(TreeNode('Abhijit' , 'app manager'))

    app_head =  TreeNode("aamir" , "application head")

    hr_head = TreeNode('Gels' , "HR Head")
    
    hr_head.add_child(TreeNode('Peter' , "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas" , "policy Manager"))
    
    CTO.add_child(infra_head)
    CTO.add_child(app_head)
    CTO.add_child(hr_head)

    # application_head.add_child(TreeNode('Dhaval' , "Cloud Manager"))
    # application_head.add_child(TreeNode('Abhijit' , 'app manager'))

 
   

    # hr_head = TreeNode('Gels' , "HR Head")
    # hr_head.add_child(TreeNode('peter' , 'recruitment manager'))
    # hr_head.add_child(TreeNode('waqas' , 'policy manager'))



    CEO.add_child(CTO)
    # root.add_child(hr_head)

    return CEO

if __name__  == "__main__":
    root = build_product_tree()
    root.print_tree("both")
    root.print_tree("name")
    root.print_tree("designation")