import os

verbose = False
def vprint(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)


def load_all_from_folder(folder):
    """
    Get all absolute file names from folder, and simply return it
    as a list of strings.
    For example, use this to load images from a folder.
    
    Parameters:
    path_to_folder {str} -- string path to parent folder
    
    Tip:
        Use foxre.relist(pattern{str}, in_list) to filter!
    """
    # Get just the file names
    rel_files = os.listdir(folder)    
    # Convert to full file names
    return [os.path.join(folder, fname) for fname in rel_files]


def folder_recursion(current_root, storage_list, include_root=True):
    """
    Direct calls obsolete.
    Use list_subfolders.recursively instead.
    
    Fills storage_list with the absolute paths of folders 
    traversed down recursively from current_root.
    Folders starting with . or _ are ignored.

    Params:
    current_root {str}        --  root of folders to be traversed
    storage_list {list}       --  list to be filled with the absolute folder paths... can be empty
    include_root=True {bool}  --  should root be written to the list?

    Return:
    None

    Usage:
    lst = list()
    folder_recursion(some_path, lst)
    """
    # append root if necessary
    vprint(f"Current root: {current_root}")
    if include_root:
        storage_list.append(current_root)
    # list of absolute paths of subdirectories in current root
    # ignorres folders starting with . (hidden) and _ (such as __pycache__)
    abs_subdirs_now = [
        os.path.join(current_root, rel_subdir) for rel_subdir in os.listdir(current_root) 
        if os.path.isdir(os.path.join(current_root, rel_subdir)) and rel_subdir[0] not in '._' and rel_subdir != "venv"
        ]
    vprint(f"\nSubdirs now:\n{abs_subdirs_now}\n")
    for abs_subdir in abs_subdirs_now:
        storage_list.append(abs_subdir)
        folder_recursion(abs_subdir, storage_list, include_root=False)

def list_subfolders_recursively(root, include_root=True):
    """
    Returns a list of all subfolders obtained recursively.
    Writes absolute paths.
    
    This function is just a wrapper around folder_recursion to allow simple x=fun(y) usage.

    Params:
        root {str}                  --  path of top level folder
        include_root=True {bool}    --  should root folder be written to the list?

    Returns:
        {list of strings}           -- absolute paths of all subfolders
    """
    lst = list()
    folder_recursion(root, lst, include_root=include_root)
    return lst

def list_files_recursively(root, include_root=True):
    """
    Returns a list of all files within subfolders.
    
    Params:
        root {str}                  --  path of top level folder
        include_root=True {bool}    --  should contents of root folder be written?

    Returns:
        {list of strings}           -- absolute paths of files within subfolders
    """
    lst = list()
    subfolders = list_subfolders_recursively(root, include_root)
    for folder in subfolders:
        file_candidates = os.listdir(folder)    # contains relative paths
        file_candidates = [os.path.join(folder, relname) for relname in file_candidates]
                                                # the paths are now absolute
        for file_candidate in file_candidates:
            if os.path.isfile(file_candidate):
                lst.append(file_candidate)
    return lst
