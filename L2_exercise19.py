'''
Advanced List Sort

Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

Notes
The sublists should be returned in the order of each element's first appearance in the given list.
'''

def advanced_sort(original_list):
    list_count_dict = {}
    for i in original_list:
        list_count_dict[i] = original_list.count(i)

    new_list = []
    for k in list_count_dict:
        new_list.append([k]*list_count_dict[k])
               
    return new_list

print(advanced_sort([2, 1, 2, 1]))
print(advanced_sort([5, 4, 5, 5, 4, 3]))
print(advanced_sort(["b", "a", "b", "a", "c"]))


'''
Sample Code:

def advanced_sort(lst):
    return [[i] * lst.count(i) for i in sorted(set(lst), key=1st.index)]
'''