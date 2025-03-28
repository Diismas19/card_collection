def sum_dicts(dict1,dict2):
    '''A function that sums the values of keys of two dictionaries.'''
    for key,value in dict2.items():
        if key in dict1.keys():
            dict1[key]+=value
        else:
            dict1[key]=value
    return dict1   

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
            item=item.split()
            card_count=item[0]
            card_name_list=item[1:]
            card_name=' '.join(card_name_list)
            if card_name in cards_dict.keys():
                cards_dict[card_name]+=int(card_count)
            else:
                cards_dict[card_name]=int(card_count)
    return cards_dict

def add_to_file(path_of_file_to_add,path_of_file_to_be_added):
    dict_to_add=get_dict(path_of_file_to_add)
    dict_of_file=get_dict(path_of_file_to_be_added)
    sum_of_dicts=sum_dicts(dict_to_add,dict_of_file)
    write_in_file(sum_of_dicts,path_of_file_to_be_added)
    print(f'Deck, located in {path_of_file_to_add}, added sucessfully on {path_of_file_to_be_added}.')