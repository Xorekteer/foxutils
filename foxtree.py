class Branch():

    def __init__(self, parent=None, children=[], content=None):
        self.children = children
        self.parent   = parent
        self.content  = content

    def add_child(self, content=None):
        """ 
        Add child branch.
        
        Kwargs:
            content {any} - content of the child
        """
        child = Branch(parent=self, content=content, children=[])
        self.children.append(child)
        return child

    def unravel(self, depth=None, to_print=False):
        "Traverse the tree down and print all children recursively, breadth first. Also prints start node."
        if to_print:
            print(self.content)
        # no children: return 
        if self.children == []:
            print(f"Tree ended")
            return None
        # children exists, specified depth
        if depth:
            return [child.unravel(depth=depth-1, to_print=to_print) for child in self.children]
        # children exists, full depth
        return [child.unravel(depth=None, to_print=to_print) for child in self.children]

    def climb(self, height=None, to_print=False):
        """ Climb the tree and print each node, incl the starting node."""
        if to_print:
            print(self.content)
        # no parent: return 
        if self.parent == None:
            print(f"Tree ended: root reached")
            return None
        # children exists, specified depth
        if height:
            return self.parent.climb(height=height-1, to_print=to_print)
        # children exists, full depth
        return self.parent.climb(height=None, to_print=to_print)
        

    def __repr__(self):
        return f"Branch:{self.content}"



if __name__ == "__main__":
    root = Branch(content="God")
    adam = root.add_child(content="Adam")
    eve  = root.add_child(content="Eve")
    abe  = eve.add_child(content="Abraham Lincoln")
    root.unravel(to_print=True)
    abe.climb(to_print=True)
    

