def extract(infile_path):
    """ 
    Takes a text file with whitespace separated elements, and returns the
    elements in a 2D array matching the whitespace separation.

    Parameters: 
        infile_path {str}   -- path to file containing text elements separated by whitespaces

    Return:
        {list of lists} -- 2D array with elements. Refer to them as res[row][column].
    """
    res = list()
    with open(infile_path, 'r') as infile:
        lines = infile.readlines()
        
        for line in lines:
            #print(line)
            res.append(list())  # append line 
            
            spacing = True
            spacing_ended = True
            for charindex in range(len(line)):

                # we don't wan't newlines
                if line[charindex] == "\n":     
                    continue    

                # -----------
                # Spacing managed in this block

                # Conditions
                # if current is space and next is space or tab
                cond1 = (line[charindex] == " " and (line[charindex + 1] == " " or line[charindex + 1] == "\t"))
                # current is tab
                cond2 = (line[charindex] == "\t")

                # Set spacing if either condition is true:
                if cond1 or cond2:
                    spacing = True
                
                # End spacing if current is not space or tab
                if spacing and line[charindex] not in [" ", "\t"]:
                    spacing       = False
                    spacing_ended = True
                
                # -----------
                
                # Spacing within line ended
                #print(res)
                if not spacing:
                    if spacing_ended:
                        spacing_ended = False
                        res[-1].append(list())  # new cell
                    res[-1][-1].append(line[charindex])

        # We finished reading, now all we have to do is merge together the characters in the >
        # innermost dimensions of res, so we get a 2D matrix with the cells inside
        for line_index in range(len(res)):
            for cell_index in range(len(res[line_index])):
                res[line_index][cell_index] = ''.join(res[line_index][cell_index])

    return res

if __name__ == "__main__":
    print(extract("intest.txt"))