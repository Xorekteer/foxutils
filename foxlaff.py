import os

def load_all_from_folder(folder):
    """
    Get all file names from folder, and simply return it
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
