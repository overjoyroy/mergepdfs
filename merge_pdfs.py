#!/usr/bin/env python
################################################################################
################################################################################
# Author: Joy Roy
# Date: October 18, 2024
# Description:The following script was written by Joy to compile all the pdfs he
# had in one folder into a single pdf.
# Input: A path to a directory of pdfs, an output filename/path (Default CWD)
# Output: A single pdf file

# Note: Yes I know there are free versions of this online, but this feels more
# secure to me. It avoids watermark and others scanning/storing my documents.

# Note: For added convenience, add to path in your .bashrc !
################################################################################
################################################################################

import argparse
import os
from PyPDF2 import PdfMerger
import re 

DEFAULT_OUTFILE_NAME = 'merged_output.pdf'

## Sorts things nice so 1,2,11,12,24 are in correct order. 
def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


def merge_pdfs_in_path(path, output_filename, verbose=False):

    # Find all PDF files in the specified path and sort them by filename
    pdf_files = sorted_nicely([f for f in os.listdir(path) if f.endswith('.pdf')])

    # Initialize a PDF merger object
    merger = PdfMerger()

    # Iterate over the sorted PDF files and add them to the merger
    for pdf in pdf_files:
        full_path = os.path.join(path, pdf)
        if verbose:
            print(f"Adding {pdf} to the merger")
        merger.append(full_path)

    # Output the merged PDF
    output_path = os.path.join(path, output_filename)
    merger.write(output_path)
    merger.close()

    numfile = len(pdf_files)
    print(f"\nSuccessfully merged {numfile} PDF files from the directory '{path}' into the output file '{output_path}'.")

def vet_inputs(args):
    
    # Ensure input path is valid and convert to absolute path
    args.path = os.path.abspath(os.path.expanduser(args.path))
    if not os.path.isdir(args.path):
        raise ValueError(f"The provided path '{args.path}' is not valid.")

    # If output is a simple filename without a directory, 
    # assume it's in the current working directory
    if os.path.dirname(args.output) == '':
        args.output = os.path.join(os.getcwd(), args.output)

    # Convert output to an absolute path
    args.output = os.path.abspath(os.path.expanduser(args.output))
    
    # Ensure the output directory exists
    dirname = os.path.dirname(args.output)
    if not os.path.exists(dirname):
        print(f"Output directory '{dirname}' does not exist. Creating it now.")
        os.makedirs(dirname, exist_ok=True)

    # If user just gave path and no filename, add default filename
    if os.path.basename(args.output) == '':
        args.output = os.path.join(args.output, DEFAULT_OUTFILE_NAME)

    # If user gave filename without correct extension
    if args.output[-4:] != '.pdf':
        args.output = args.output + '.pdf'
    
    return args


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge all PDFs in a given directory.")
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument("path", help="Path to the directory containing PDFs")
    parser.add_argument("output", help="Name of the output merged PDF file (default: merged_output.pdf)")
    parser.add_argument("-v", "--verbose", action='store_true', help="Use if you want to log more to console")

    # Parse the command-line arguments
    args = parser.parse_args()
    args = vet_inputs(args)

    # Call the merge function with the provided path and optional output filename
    merge_pdfs_in_path(args.path, args.output, args.verbose)
