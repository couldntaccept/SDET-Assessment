# Write a solution to find the character that has the highest number of occurrences within a certain string, ignoring
# case. If there is more than one character with equal highest occurrences, return the character that appeared first
# within the string.

def find_max_occurence(str):
    ls = list(str.lower())
    max(ls,key=ls.count)
    return ls[0]