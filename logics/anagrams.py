# All the worlds are matching or not in anagra
s1 = "Sabbha"
s2 = "ahbSba"
s3 = "Sachi"


def anagrams(s1: str, s2: str) -> bool:
    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    return False


print(anagrams(s1, s2))
print(anagrams(s1, s3))