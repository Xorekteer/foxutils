import re

def split_sentences(in_str):
    """Splits the input string to sentences

    Arguments:
        in_str {string}     -- input string

    Returns:
        {list of strings}   -- List of sentences.
    """
    # The pattern is puntctuation followed by space
    pattern = re.compile(r"(\. |\? |! )")  
    matches = re.finditer(pattern, in_str)
    result = []     # list of sentences
    cur_pos = 0     # current position
    for match in matches:
        end = match.span()[1]   # end is the character AFTER the space
        result.append(in_str[cur_pos:(end-1)])
        cur_pos = end
    result.append(in_str[cur_pos:])
    return result

def relist(re_str, in_list):
    """
    Filters a list using a regex pattern. 
    Elements that weren't completely rejected go in the new list.
    
    Args:
        re_str {string}             -- regex pattern to be compiled
        in_list {list of strings}   -- list to be filtered 
    
    Returns:
        {list of strings}           -- all list elements inside which regex found a match
    """
    newlist = []
    for elem in in_list:
        if re.findall(re_str, elem) != []:
            newlist.append(elem)
    return newlist
    

def reword(re_str="", in_str=""):
    """Returns words from a string that aren't rejected by regex.

    Args:
        re_str {string}:    -- regex string
        in_str {string}:    -- input string

    Returns:
        {list of strings}   -- list of words inside which regex found a match
    """
    word_list = in_str.split(sep=" ")
    return relist(re_str, word_list)

def resentence(re_str, in_str):
    """Return sentences that weren't rejected by regex.
    Removes 

    Args:
        re_str {string}     -- regex string
        in_str {string}     -- input string

    Returns:
        {list of strings}   -- list of senteces inside which regex found a match
    """
    return relist(re_str, split_sentences(in_str))
