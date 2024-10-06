s = "Sabbha"

# r = s[::-1].lower()
#
# print(r)

for i, v in enumerate(s):
    print((s[i::], s[i::-1], s[i], s[i+1:]))
    if s[i] in s[i+1:]:
        print(s[i], s[::-i-1])