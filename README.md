# mergepdfs

Author: Joy Roy

Date: October 18, 2024

### Description
This Python script merges all PDF files from a specified directory into a single output PDF. The motivation behind writing this script was to avoid potential privacy concerns and watermarks that come with using free online PDF merging services. With this script, all processing is done locally on your machine, providing greater security. I mostly only wrote this for my own use.

### Features
Merges all PDFs in a given directory into a single PDF file.
Orders the files numerically in human-friendly sorting (e.g., 1, 2, 11, 12, 24).
Outputs the merged file to a user-specified location (default: current working directory).
Verbose mode for logging the process to the console.

### Requirements

Python 3.x

PyPDF2 library

### Usage

To merge all PDF files in a directory, run:

```
python merge_pdfs.py /path/to/pdfs /path/to/merged_output.pdf
```

The following omits the path to the output but defaults to the current directory:
```
python merge_pdfs.py /path/to/pdfs merged_output.pdf
```

To see all the files being merged, use verbose mode:

```
python merge_pdfs.py /path/to/pdfs merged_output.pdf -v
```


