if False:   # VS code linting trick
    import foxtag
    import foxtrix
    
# actual imports
import x_foxport
import foxutils.webtools.foxtag  as foxtag
import foxutils.webtools.foxtrix as foxtrix

outfile_path = "foxstrap_out.txt"
infile_path  = "foxstrap_in.txt"

def boot_table():
    """
    Generates a bootstrap table from a text file.
    Uses a <div class="container" style="float:left;"> as root

    Use PAD as text to leave inner_html empty
    """
    # Get input from textfile
    in_array = foxtrix.extract(infile_path)     # get input in array form from txt
                                                # can be dereferenced using in_array[row_index][col_index]
    
    root = foxtag.Elem(tag='div', attrs='class="container", style="float:left;"')
    for row_index in range(len(in_array)):
        row_child = root.add_child(tag='div', attrs='class="row"')
        
        for col_index in range(len(in_array[row_index])):

            inner_html = in_array[row_index][col_index]
            if inner_html == "PAD":
                inner_html = ""
            
            row_child.add_child(tag='div', attrs='class="col"', inner_html=inner_html)
            
    with open(outfile_path, 'w') as outfile:    
        outfile.write(foxtag.write_from_top())
        

def boot_form(form_name='form'):
    """
    Generates a bootstrap form from a text file.
    
    Text file must contain a single WTForm variable name per row.
    
    Uses a <form method=POST action=""> as root.
    """
    # Get input from textfile
    in_array = foxtrix.extract(infile_path)     # get input in array form from txt
                                                # can be dereferenced using in_array[row_index][col_index]
    
    # outer <form>
    root = foxtag.Elem(tag='form', attrs='method="POST" action=""')
    # starting hidden_tag
    root.inner_html = r"{{form.hidden_tag()}}"
    # repetitive rows/cols
    for row_index in range(len(in_array)):
        row_child = root.add_child(tag='div', attrs='class="row"')
        
        label   = "{{" + form_name + "." + in_array[row_index][0] + ".label" + "}}"
        field   = "{{" + form_name + "." + in_array[row_index][0] + "}}"
        row_child.add_child(tag='div', attrs='class=col', inner_html=label)
        row_child.add_child(tag='div', attrs='class=col', inner_html=field)
    # submit field in a container
    submit_div_child = root.add_child(
        tag='div',
        attrs='class=container style="float:left;"',
        inner_html='{{ form.submit }}'        
        )
        
    err_str_list = []
    for row_index in range(len(in_array)):
        variable = in_array[row_index][0]
        err_str = (
            f"<!-- Errors in {variable}  -->\n"
            f"{{% if form.username.errors %}}\n"
            f"    <span> Errors in {variable}: </span> <br>\n"
            f"    {{% for error in form.{variable}.errors %}}\n"
            f'        <div class="alert alert-secondary">\n'
            f'            {{{{error}}}}\n'
            f'        </div>\n'
            f'    {{% endfor %}}\n'
            f'{{% endif %}}\n'
            )
        err_str_list.append(err_str)

    with open(outfile_path, 'w') as outfile:    
        outfile.write(foxtag.write_from_top())
        outfile.write("".join(err_str_list))




        
if __name__ == "__main__":
    boot_form()
