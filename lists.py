def remove_elements(list_to_remove_elements):
    len_elem = len(list_to_remove_elements)
    if len_elem >= 6 :
        del list_to_remove_elements[4:6]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len_elem == 5 :
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len_elem >= 1 and len_elem <= 5 :
        del list_to_remove_elements[0]
        del list_to_remove_elements[4:]
        return list_to_remove_elements
    elif len_elem >= 1 and len_elem < 4 :
        del list_to_remove_elements[0]
    elif len_elem < 1 :
        return list_to_remove_elements


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements


def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    len_1 = len(list_to_compare1)
    len_2 = len(list_to_compare2)
    if len_1 >= 3 and len_2 >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    sublist0 = list_of_lists_to_modify[0]
    sublist1 = list_of_lists_to_modify[1]
    sublist2 = list_of_lists_to_modify[2]
    len_sublist0 = len(sublist0)
    len_sublist1 = len(sublist1)
    len_sublist2 = len(sublist2)
    if len_sublist0 >= 0:
        sublist0 = sublist0[0:2]
    else: 
        sublist0 = []
    if len_sublist1 >= 2:
        sublist1 = sublist1[1:4]
    else:
        sublist1 = []
    if len_sublist2 >= 0:
        sublist2 = sublist2[-2:]
    return list_of_lists_to_modify
