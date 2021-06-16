# the function below will claim that the characters are unique 
# because the bug is in the function only checks consecutive 
# characters

def unique(characters):
    i = 1
    temp = ""

    if characters == "":
        return True

    while i < len(characters):
        if characters[i] != characters[i - 1]:
            temp = characters[i]
            i += 1
        else:
            return False
    return True

print(unique('goo'))
print(unique('abcdefg'))
print(unique(''))
print(unique('adba'))

############################

# utilizing the set data structure will help identify unique characters

def unique_v2(characters):
    return len(set(characters)) == len(characters)

print(unique_v2('adba'))


# utilizing set but we manually check for the uniqueness
### whiteboard the code below

def unique_v3(characters):

    chars = set()

    for letter in characters:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True
