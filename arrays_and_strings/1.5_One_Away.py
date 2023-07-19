# Runtime complexity O(1) if the first if statement is true because if the length of the 
# strings differ by more than 1. This operation is constant time because finding 
# the length of a string is constant time in python. 

# The other two functions 'one_edit_replac'e' and 'one_edit insert' both iterate through each 
# character in the string once. Resulting in a runtime complexity of O(n)

# Since the functions 'one_edit_replace(s1, s2)' and 'one_edit_insert(s1, s2)' are never both 
# called in a single call to 'one_away(s1, s2)', the overall worst-case runtime complexity is O(N),
# where N is the length of the strings.


def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    elif len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    else:
        if len(s1) < len(s2):
            return one_edit_insert(s1, s2)
        else:
            return one_edit_insert(s2, s1)
        

def one_edit_replace(s1, s2):
    edited = False

    for c1, c2 in zip(s1,s2):
        if c1 != c2:
            if edited:
                return False
            else:
                edited = True

    return True 

def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            else:
                edited = True
                j+=1
        else:
            i+=1
            j+=1

    return True


print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))