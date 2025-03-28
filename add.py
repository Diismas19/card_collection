import sys
from functions import add_files

if len(sys.argv) != 3:
    print('Usage: python3 add.py <path_of_file_to_add> <path_of_file_to_be_added>')
    sys.exit(1)

add_files(sys.argv[-2],sys.argv[-1])