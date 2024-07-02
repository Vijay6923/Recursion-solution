def fix_caps_lock(word):
    if word.isupper() or (word[0].islower() and word[1:].isupper()):
        return word.swapcase()
    return word


input = input()
print(fix_caps_lock(input))