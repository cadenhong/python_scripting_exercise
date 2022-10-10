'''
Scrambled Letters

Write a function that receives a list of words and a mask. Return a list of words, sorted alphabetically, that match the given mask.

Examples
scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "*re**") ➞ ["creed"]
scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "***") ➞ ["dee", "ree"]

Notes
The length of a mask will never exceed the length of the longest word in the word list.
'''

def scrambled(words, mask):
    sorted_words = []

    for word in words:
        if len(word) == len(mask):
            for i in range(int(len(word))):
                if mask[i] == '*' or mask[i] == word[i]:
                    continue
                else: break
            sorted_words.append(word)

    return sorted(sorted_words)

print(scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "*re**"))
print(scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "***"))


'''
Sample Code:

import re; scrambled = lambda w, m: [i for i in w if re.match("^"+m.replace('*', r'\w')+"$", i)]
'''