import sys
from functions import get_dict_of_cards, get_sum_of_dicts, get_new_lines

if len(sys.argv) != 2:
    print('Usage: python3 add.py <path_to_file>')
    sys.exit(1)

collection=get_dict_of_cards('./collection.txt')

deck_to_add=get_dict_of_cards(sys.argv[-1])

new_collection=get_sum_of_dicts(collection,deck_to_add)

with open('./collection.txt','w') as file:
    file.writelines(get_new_lines(new_collection))