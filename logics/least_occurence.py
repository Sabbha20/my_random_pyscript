s = "abracadabra"

# lst = [(s.count(ele)) for ele in s]
# min_val = min(lst)
# lst1 = [ele for ele in s if s.count(ele) == min_val]
# print(lst)
# print(min(lst))
# print(list(set(lst1)))


def least_occurence(s):
    min_val = min((s.count(ele)) for ele in s)
    lst = [ele for ele in s if s.count(ele) == min_val]
    if len(lst) > 1:
        return list(set(lst))
    return lst[0]

print(least_occurence(s))
