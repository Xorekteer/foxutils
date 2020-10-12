if False:   # VS code linting trick
    import sys
    sys.path.append('..')
    import foxcast

import x_foxport
import foxutils.foxcast as foxcast




class Document():
    """
    Wrapper around HTML nodes.

    Methods:
        .__init__(indent_by='\t')         
            -- returns a document
            indent_by = '\t' {str}  -- indent string to used when writing a document 

        .write_from_top()   -- returns a {string} of html code w/ the defined tag structure
    """

    def __init__(self, indent_by = '\t'):
        self.counter = 0
        self.instances = list()
        self.indent_by = indent_by

    def recursive_write(self, root, res):
        indent = self.indent_by
        tabs = indent * root.level

        # Tag
        if root.attrs != '':
            attrs_space = ' '
        else:
            attrs_space = ''
        res.append(tabs + '<' + root.tag + attrs_space + root.attrs + '>\n')

        # InnerHTML
        if root.inner_html != '':
            res.append(tabs + indent +  root.inner_html + '\n')

        # Children
        for child in root.children:
            next_res = list()
            res.append(next_res)
            self.recursive_write(child, next_res)

        res.append(tabs + '</' + root.tag + '>\n')

    def write_from_top(self):
        """ Wrapper around recursive_write() """
        root = self.instances[0]
        res = list()
        self.recursive_write(root, res)
        return ''.join(foxcast.flatten_iterable(res))



class Elem():
    """
    Class for storing html nodes.

    Constructor kwargs / instance parameters (same name):
        tag         {str}         --  name of html tag
        attrs       {str}         --  attributes inside html tag
        inner_html  {str}         --  text between opening tag and closing tag of current elem        >
                                  --  avoid use w/ children (in theory, content added after children) |
        parent {self.__class__}   --  parent of element

        document=None {Document}  --  document holding the Node >
                                  --  if the node has a parents, it's added to the same document >
                                  --  if the node has no parent (is a root node), document has to be specified as a kwarg >
                                  --  throws error
        
    Methods:
        .add_child(tag='', attrs='', inner_html='')
            -- adds child to current
            -- return the child {self.__class__}

    Usage:
        doc  = Document()                       -- document frame constructor
        root = self.__class__(document=doc)     -- constructor
        a    = root.add_child()                 -- add children as desired
        __class__.write_from_top()              -- write content...
                                                -- wrap in print to display in terminal
    """

    def __init__(self, parent=None, tag='', attrs='', inner_html='', document=None):
        self.tag        = tag
        self.attrs      = attrs
        self.inner_html = inner_html

        self.children = list()

        self.parent = parent
        if parent:
            self.level     = parent.level + 1
            self.document  = parent.document     # each node (Elem) is part of a document
        else:
            self.level     = 0
            self.document  = document            # specify document as kwarg if the node is a root
                                             
        try:
            self.document.instances.append(self)
        except AttributeError:
            print(
                f"You likely tried to create a root node without a document frame.  Please don't do that.\n"
                f"Root nodes should be given a Document as a kwarg."
            )

    def add_child(self, tag='', inner_html='', attrs=''):
        new_child = self.__class__(parent=self, tag=tag, inner_html=inner_html, attrs=attrs)
        self.children.append(new_child)
        return new_child




if __name__ == "__main__":
    doc = Document()
    root = Elem(tag='div', document=doc)
    root.document = doc
    c1 = root.add_child(tag='p', inner_html="content1")
    c2 = root.add_child(tag='table')
    c2.add_child('p', inner_html='content2')
    c2.add_child('p', attrs='style="margin-top: 10px;"', inner_html='special content')
    print(doc.write_from_top())
