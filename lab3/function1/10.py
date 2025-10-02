def unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

#Example
print(unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))