# code is still a work in progress, will be released publicly once completed and tested on both a test case file and then an instance of actual data

import os
import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def string_splitter(file1, file2):
    with open(file1, 'r') as infile:
        input_cwd = os.path.dirname(file1)
        ori_list1 = infile.readlines()
        for line in ori_list1: # now for writing the actual file
            line = line.replace('  ', '    ') # evens out the spacing for splitting purposes
            line = re.split('    ', line) # splits line
            init_seq_1 = line[3] # pick line 3, this should be the DNA sequence, because for whatever reason DNA is that line
            init_peptide_1 = line[0]
    with open(file2, 'r') as infile2:
        input_cwd = os.path.dirname(file2)
        ori_list2 = infile2.readlines()
        for line2 in ori_list2: # now for writing the actual file
            line2 = line.replace('  ', '    ') # evens out the spacing for splitting purposes
            line2 = re.split('    ', line) # splits line
            init_seq_2 = line2[3] # pick line 3, this should be the DNA sequence, because for whatever reason DNA is that line
            init_peptide_2 = line2[0]
    with open(input_cwd + '\\' + 'RFComb_' + (os.path.basename(file1)), 'w') as outfile:
        splitCombiner(init_seq_1, init_peptide_1, init_seq_2, init_peptide_2)


def splitCombiner(init_seq_1, init_peptide_1, init_seq_2, init_peptide_2):
    for string in ori_list2:
        if(re.match(init_peptide_1, string)):
            string_match = string
            string_match = string_match.replace('  ', '    ') # evens out the spacing for splitting purposes
            string_match = re.split('    ', string_match) # splits line
            lineval_comb = line[2] + string_match[2]
            
            finalSeq_comp = ''.join([protein, "    ", line[2], "  ", forSeq, "\n"]) # put it all together, that's it
            outfile.write(finalSeq_comp) # write it
        else:
        
# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')

def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file1 = fd.askopenfilenames(
        title='Load files',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected Files',
        message=file1
    )
def select_files2():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file2 = fd.askopenfilenames(
        title='Load files',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected Files',
        message=file2
    )
# Load First File button
open_button = ttk.Button(
    root,
    text='Load First File',
    command=select_files
)
# Load Second File button
open_button = ttk.Button(
    root,
    text='Load Second File',
    command=select_files2
)

# start process button
combine_button = ttk.Button(
    root,
    text = 'Combine Files',
    command = string_splitter)

open_button.pack(expand=True)

root.mainloop()
