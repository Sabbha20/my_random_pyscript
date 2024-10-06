# AIM - Remove duplicates from the string


s = "Sabbha Sachi Mondal"


def remove_duplicates(s):
    lst = []
    for ele in s:
        if ele not in lst:
            lst.append(ele)
    return "".join(lst)

# print(f"lst:\t {lst}")
# print(f"s1:\t {s1}")
print(remove_duplicates("HelloWorld"))