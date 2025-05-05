import os

def sum_dicts(dict1,dict2):
    '''A function that sums the values of keys of two dictionaries.'''
    for key,value in dict2.items():
        if key in dict1.keys():
            dict1[key]+=value
        else:
            dict1[key]=value
    return dict1

def minus_dicts(dict1,dict2):
    '''A function that maths dict1 - dict2.'''
    for key,value in dict2.items():
        if key in dict1.keys():
            dict1[key]-=value
        else:
            dict1[key]=-value
    return dict1

def overlap_dicts(dict1,dict2):
    '''A function that returns the content that are in both dicts.'''
    both_dict={}
    for key in dict1.keys():
        if key in dict2.keys():
            if dict1[key] >= dict2[key]:
                both_dict[key]=dict2[key]
            else:
                both_dict[key]=dict1[key]
    return both_dict

def write_in_file(dict,path_to_file):
    '''A function that write a dict on a file.'''
    lines=[]
    for key,value in dict.items():
        line=f'{value} {key}'+'\n'
        lines.append(line)
    with open(path_to_file,'w') as file_to_be_written:
        file_to_be_written.writelines(lines)

def get_dict(path_to_file):
    '''A function that makes a dictionary with the cards and quantities of a MTGO format .txt file.'''
    cards_dict={}
    with open(path_to_file,'r') as card_list:
        lines=card_list.readlines()
        for item in lines:
            if item == '\n':
                lines.remove(item)
        for item in lines:
            item=item.split()
            card_count=item[0]
            card_name_list=item[1:]
            card_name=' '.join(card_name_list)
            if card_name in cards_dict.keys():
                cards_dict[card_name]+=int(card_count)
            else:
                cards_dict[card_name]=int(card_count)
    return cards_dict

def clean_dict(dict):
    '''A function that take out the keys with values <= 0'''
    del_list=[]
    for key in dict.keys():
        if dict[key] <= 0:
            del_list.append(key)
    for item in del_list:
        del dict[item]
    return dict

def print_dict(dict):
    '''A function that prints a dict in the format mtgo.txt'''
    for key,value in dict.items():
        print(f'{value} {key}')

def add_files(path_of_file_to_be_added,path_of_file_to_add):
    '''A function that add the content of two files. If file to be written doesn't exist, the function will create it.'''
    if os.path.exists(path_of_file_to_be_added) == False:
        with open(path_of_file_to_be_added,'w') as file:
            file.writelines([])
    dict_to_add=get_dict(path_of_file_to_add)
    dict_to_be_added=get_dict(path_of_file_to_be_added)
    sum_of_dicts=sum_dicts(dict_to_add,dict_to_be_added)
    write_in_file(sum_of_dicts,path_of_file_to_be_added)
    print(f'Deck located in {path_of_file_to_add}, added sucessfully on {path_of_file_to_be_added}.')

def take_out_file(path_big_file,path_small_file):
    '''A function that take out that cards that are in the small file from the big file.'''
    big_dict=get_dict(path_big_file)
    small_dict=get_dict(path_small_file)
    for key,value in small_dict.items():
        if value > big_dict[key]:
            raise Exception(f'You have more {key} copies on the small file than in the big file.')
        else:
            big_dict[key]-=value
    clean_dict(big_dict)
    write_in_file(big_dict,path_big_file)
    print(f'The list in {path_small_file} has sucessfully deduced the cards from {path_big_file}.')

def compare_files(path_to_file_1,path_to_file_2):
    dict_1=get_dict(path_to_file_1)
    dict_2=get_dict(path_to_file_2)
    both_dict=overlap_dicts(dict_1,dict_2)
    minus_dicts(dict_1,both_dict)
    clean_dict(dict_1)
    if len(dict_1) == 0:
        print(f'There are no cards that are only in {path_to_file_1} file')
    else:
        print(f'The cards that are only in the {path_to_file_1} file are:')
        print_dict(dict_1)
    minus_dicts(dict_2,both_dict)
    clean_dict(dict_2)
    if len(dict_2) == 0:
        print(f'There are no cards that are only in {path_to_file_2} file')
    else:
        print(f'The cards that are only in the {path_to_file_2} file are:')
        print_dict(dict_2)
    if len(both_dict) == 0:
        print('There are no cards that are in both lists.')
    else:
        print('The cards that are in both files are:')
        print_dict(both_dict)