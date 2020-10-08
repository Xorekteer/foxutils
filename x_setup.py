#!/usr/bin/env python3

"""
This is a utility designed to eliminame the discord of import in foxutils.

How it works:
Basically creates/updates a file "x_foxport.py" in every subfolder, which is then subsequently imported by the scripts themselves.
Run this script every time foxutils is moved.
If a script is used by copying, make sure to copy an "x_foxport.py" along with it.
This way a script within this library can refer to another script within this library without
making assumptions about its own path.


may the fox be with you

/\ /\   <3
  
  V 
"""

import os
import foxlaff
import datetime

if __name__ == "__main__":
    cwd = os.getcwd()
    lst = list()
    folders_in_library = foxlaff.list_subfolders_recursively(cwd)
    # determine the import command to be written
    os.chdir('..')
    parent_of_foxutils = os.getcwd()
    import_command = (
        f"# generated by foxutils.x_setup\n"
        f"# please rerun script on library move\n"
        f"# last updated: {datetime.datetime.now()}\n"
        f"import sys\n"
        f"sys.path.append(\"{parent_of_foxutils}\")\n"
    )
    
    for folder in folders_in_library:
        with open(os.path.join(folder, "x_foxport.py"), 'w') as write_file:
            write_file.write(import_command) 
    
    
    print("Setup Done")