def get_dict_of_cards(path_to_file):
    cards_dict={}
    with open(path_to_file,'r') as cards_file:
        lines=cards_file.readlines()
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

def get_sum_of_dicts(dict_1,dict_2):
    for key,value in dict_2.items():
        if key in dict_1.keys():
            dict_1[key]+=value
        else:
            dict_1[key]=value
    return dict_1

def get_new_lines(dict):
    linhas=[]
    for key,value in dict.items():
        linha=f'{value} {key}'+'\n'
        linhas.append(linha)
    return linhas