if False:   # VS code linting trick
    import sys
    sys.path.append('..')
    import foxcast

import x_foxport
import foxutils.foxcast as foxcast


class Elem():
    """
    Class for storing html trees.

    Constructor kwargs / instance parameters (same name):
        tag         {str}   --  name of html tag
        attrs       {str}   --  attributes inside html tag
        inner_html  {str}   --  text between opening tag and closing tag of current elem        >
                            --  avoid use w/ children (in theory, content added after children) |
        parent {self.__class__} -- parent of element
        

    Methods:
        .add_child(tag='', attrs='', inner_html='')
            -- adds child to current
            -- return the child {self.__class__}

        .write_from_top()
            -- returns a {string} of html code w/ the defined tag structure
    
    Usage:
        root    = self.__class__()      -- constructor
        a       = root.add_child()      -- add children as desired
    """
    indent_by = '\t'
    counter = 0
    instances = list()


    def __init__(self, parent=None, tag='', attrs='', inner_html=''):
        self.children = list()

        self.id = self.__class__.counter
        self.__class__.counter += 1
        
        self.tag = tag
        self.attrs = attrs
        self.inner_html = inner_html

        self.parent = parent
        if parent:
            self.parent_id = parent.id
            self.level = parent.level + 1
        else:
            self.parent_id = None
            self.level = 0
        
        self.__class__.instances.append(self)


    def add_child(self, tag='', inner_html='', attrs=''):
        new_child = Elem(parent=self, tag=tag, inner_html=inner_html, attrs=attrs)
        self.children.append(new_child)
        return new_child

def recursive_write(root, res):
    indent = Elem.indent_by
    tabs = indent * root.level
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
        recursive_write(child, next_res)


    res.append(tabs + '</' + root.tag + '>\n')

def write_from_top():
    """ Wrapper around recursive_write() """
    root = Elem.instances[0]
    res = list()
    recursive_write(root, res)
    return ''.join(foxcast.flatten_iterable(res))

if __name__ == "__main__":
    root = Elem(tag='div')
    c1 = root.add_child(tag='p', inner_html="content1")
    c2 = root.add_child(tag='table')
    c2.add_child('p', inner_html='content2')
    c2.add_child('p', attrs='style="margin-top: 10px;"', inner_html='special content')
    print(write_from_top())
