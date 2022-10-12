'''
Get Students with Names and Top Notes

Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }
top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }
top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
'''

def top_note(input_dict):
    output_dict = {}
    output_dict["name"] = input_dict["name"]
    output_dict["top_note"] = sorted(input_dict["notes"])[-1]
    return output_dict

print(top_note({ "name": "John", "notes": [3, 5, 4] }))
print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))

'''
Sample Code:

def top_note(student):
    return {"name":student["name"], "top_note": max(student["notes])}
'''