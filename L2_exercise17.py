'''
Find the Pattern

Given a dictionary containing up to six phrases, return a list containing the matching phrases according to the given string (p). Ignore any digit that is placed after or before the given string.

Whether the first letter is capitalized or not, if all letters of the word match the given string (p), it is valid. If it does not match the given string (p) then None.

Examples
find_pattern({
"Phrase1": "COVID-19 is no good",
"Phrase2": "COVID-18 is no good",
"Phrase3": "COVID-17 is no good"
}, "COVID-19")
➞ ["Phrase1 = COVID-19", "Phrase2 = None", "Phrase3 = None"]

find_pattern({
"Phrase1": "Edabit is great",
"Phrase2": "Edabit is very great",
"Phrase3": "Edabit is really great"
}, "really")
➞ ["Phrase1 = None", "Phrase2 = None", "Phrase3 = really"]
'''

def find_pattern(phrases, pattern):
    matching_phrases = []

    for key in phrases:
        if pattern in phrases[key]:
            matching_phrases.append(f"{key} = {pattern}")
        else:
            matching_phrases.append(f"{key} = None")

    return matching_phrases

print(find_pattern({
"Phrase1": "COVID-19 is no good",
"Phrase2": "COVID-18 is no good",
"Phrase3": "COVID-17 is no good"
}, "COVID-19"))

print(find_pattern({
"Phrase1": "Edabit is great",
"Phrase2": "Edabit is very great",
"Phrase3": "Edabit is really great"
}, "really"))


'''
Sample Code:

from re import search, IGNORECASE
def find_pattern(dict_, p):
    return sorted("{} = {}".format(k, p if search(p, v, IGNORECASE) else None)
        for k, v in dict_.items())
'''