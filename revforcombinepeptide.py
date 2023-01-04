import re
import os
import tkinter as tk
import tkinter.filedialog as fd

def mergeFile(file, mit, temp):
    with open(file, 'r') as infile:
    
        # Generate list of lines. Iterate.
        list_lines = infile.readlines()
        for line in list_lines:
        
            # Split line.
            line = re.split('\s+', line)
            
            # Check if our line is already in the master list by checking if the sequence is already in it.                   
            
            seq_found = 0
            
            for item in mit:
                if item[1] == line[0].strip():
                    item[0] += int(line[1])
                    seq_found = 1

            # If not, add the line to the master list.
            if seq_found == 0:
                temp[1] = line[0]
                temp[0] = int(line[1])
                temp[2] = line[2].strip()
                
                mit.append(temp.copy())
                

def splitCombiner(files):

    mit = []
    temp = ["","",""]
    
    for file in files:
        mergeFile(file, mit, temp) # Call for file merger seen above.
                
    # Get directory, start writing outfile.
    input_cwd = os.path.dirname(files[0])
    with open(input_cwd + '\\' + 'RFComb_' + (os.path.basename(files[0])), 'w') as outfile:
        
        mit.sort(reverse=True) # Sort in descending order.
        for item in mit:
            outfile.write(item[1] + "\t" + str(item[0]) + "\t" + item[2] + "\n")

# Tkinter options and initial file request
root = tk.Tk()
root.withdraw()
files = fd.askopenfilenames(parent=root, title='Choose files to merge')
splitCombiner(files)
