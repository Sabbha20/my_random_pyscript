# Find the most occurring character in a string.\



s = "Sabbha Sachi Mondal"
def max_occurrence(s:str):
    max_occ = max(s.count(ch) for ch in s)
    lst = list(set(ch for ch in s if s.count(ch) == max_occ))
    if len(lst) > 1:
        return  lst
    return lst[0]

print(max_occurrence(s))