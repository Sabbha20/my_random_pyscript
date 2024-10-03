# First non-repeating character in string

s = "Sabbha Sachi Mondal"

def first_unique_character(s):
    lst = [(idx,ele) for idx, ele in enumerate(s) if s.count(ele) == 1]
    return lst[0]

print(first_unique_character(s))
