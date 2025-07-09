def merge_and_sort_lists(list1, list2):
    # Merge the two lists
    merged_list = list1 + list2
    
    # Remove duplicates by converting to a set, then back to a list
    unique_list = list(set(merged_list))
    
    # Sort the list in ascending order
    unique_list.sort()
    
    return unique_list

list_a = [3, 1, 4, 5]
list_b = [5, 6, 1, 2]

result = merge_and_sort_lists(list_a, list_b)
print(result)
