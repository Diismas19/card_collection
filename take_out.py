import sys
from functions import take_out_file

if len(sys.argv) != 3:
    print('Usage: python3 take_out.py <path_to_big_file> <path_to_small_file>')
    sys.exit(1)

take_out_file(sys.argv[1],sys.argv[2])
