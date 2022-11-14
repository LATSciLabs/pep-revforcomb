import re
import os
import tkinter as tk
import filedialogue as fd

def splitCombiner(file1, file2):

    # Declarations, mit is an empty list meaning "merge into this"
    mit = []
    temp = ["","",""]
    seq_found = 0
    
    # Open file1.
    with open(file1, 'r') as infile:
    
        # This generates a list of lines from the file.
        ori_list1 = infile.readlines()
        
        # Now we go through the list item by item, or line by line.
        for line in ori_list1:
        
            # re.split returns a list. In this step you overwrite your individual line (an element in a list) with a list of four splits.
            # CIPMSQRQC    221  TGTATTCCTATGTCGCAGCGTCAGTGT is a sample line. It is split into:
            # ["CIPMSQRQC","221","TGTATTCCTATGTCGCAGCGTCAGTGT"]
            line = re.split('\s+', line)
            
            # Next I’ll add the first to third result of the split to the master list. 
            
            temp[1] = line[0]
            temp[0] = int(line[1])
            temp[2] = line[2].strip()
            
            mit.append(temp.copy())       
    
    print(mit)
    
    # file2 should be eerily similar.
    with open(file2, 'r') as infile2:
    
        # Generate list of lines. Iterate.
        ori_list2 = infile2.readlines()
        for string in ori_list2:
        
            # Split as before.
            string = re.split('\s+', string)
            
            # Now we check if our line is already in the master list by checking if the sequence is already in it.                   
            
            seq_found = 0
            
            for item in mit:
                if item[2] == string[2].strip():
                    item[0] += int(string[1])
                    seq_found = 1

            # and if it’s not, add the line to the master list.
            if seq_found == 0:
                temp[1] = string[0]
                temp[0] = int(string[1])
                temp[2] = string[2].strip()
                
                mit.append(temp.copy())
                
    # Output.
    # Get directory, start writing outfile.
    input_cwd = os.path.dirname(file1)
    with open(input_cwd + '\\' + 'RFComb_' + (os.path.basename(file1)), 'w') as outfile:
        
        mit.sort(reverse=True) # Sorting in descending order
        for item in mit:
            outfile.write(item[1] + "\t" + str(item[0]) + "\t" + item[2] + "\n") # Write file

# tkinter, ask for file input
root = tk.Tk()
root.withdraw()
file1 = fd.askopenfilename(parent=root, title='Choose a file')
file2 = fd.askopenfilename(parent=root, title='Choose a file')
splitCombiner(file1, file2)
