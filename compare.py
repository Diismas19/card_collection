import sys
from functions import compare_files

if len(sys.argv) != 3:
    print('Usage: python3 compare.py <path_to_file1> <path_to_file2>')
    sys.exit(1)

compare_files(sys.argv[1],sys.argv[2])