import sys
from functions import add_to_file

if len(sys.argv) != 2:
    print('Usage: python3 add.py <path_to_file>')
    sys.exit(1)

add_to_file(sys.argv[-1],'./collection.txt')