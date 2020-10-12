if False:   # VS code linting trick
    import foxlaff
    import foxre
    import foxcast

# Real imports
import x_foxport    # appends foxutils root to path
                    # doesn't activate VS code linting
import foxutils.foxlaff as foxlaff
import foxutils.foxre   as foxre
import foxutils.foxcast as foxcast

import os
import re
"""
Improvement suggestion: refactor.
"""


def mangle_all_html(recursive=False):
    """
    Removes all lines that are empty or contain comments from all htmls within the current folder.
    """
    if recursive:
        subfolders     = foxlaff.list_subfolders_recursively(os.getcwd(), include_root=True)
        filenames_here = [foxlaff.load_all_from_folder( folder ) for folder in subfolders]
        filenames_here = foxcast.flatten_iterable(filenames_here)
    else:
        filenames_here = foxlaff.load_all_from_folder( os.getcwd() )
    
    html_filenames = foxre.relist("\.html", filenames_here)
    for filename in html_filenames:
        result_lines  = list()
        with open(filename, 'r') as current_file:   # open for reading
            content_lines = current_file.readlines()
            for line in content_lines:
                # Not comment and not entirely whitespace
                if not ("<!--" in line and "-->" in line or re.fullmatch("\s+", line)):
                    # Include in result
                    result_lines.append(line)
            # Write out
        with open(filename, 'w') as current_file:   # open for writing
                                                    # yes I know there is an update mode but I prefer clarity in my code
            current_file.writelines(result_lines)
            
            
def mangle_all_snek(recursive=False):
    """
    Removes all lines containing only whitespace or # comments from all python files within current folder.
    """
    if recursive:
        subfolders     = foxlaff.list_subfolders_recursively(os.getcwd(), include_root=True)
        filenames_here = [foxlaff.load_all_from_folder( folder ) for folder in subfolders]
        filenames_here = foxcast.flatten_iterable(filenames_here)
    else:
        filenames_here = foxlaff.load_all_from_folder( os.getcwd() )
    
    filenames_here = foxlaff.load_all_from_folder( os.getcwd() )
    html_filenames = foxre.relist("\.py", filenames_here)
    for filename in html_filenames:
        result_lines  = list()
        with open(filename, 'r') as current_file:   # open for reading
            content_lines = current_file.readlines()
            for line in content_lines:
                # Not comment and not entirely whitespace
                if not (re.match("(^\s+#)|(^#)", line) or re.fullmatch("\s+", line)):
                    # Include in result
                    result_lines.append(line)
            # Write out
        with open(filename, 'w') as current_file:   # open for writing
                                                    # yes I know there is an update mode but I prefer clarity in my code
            current_file.writelines(result_lines)
            
if __name__ == "__main__":
    mangle_all_html(recursive=True)
    mangle_all_snek(recursive=True)
