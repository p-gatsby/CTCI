

def palindrome_permutation(s):
    H = dict()

    # Remove all the spaces in the string
    s = s.replace(" ", "").lower()

    for i in s:
        if i in H:
            H[i] += 1
        else:
            H[i] = 1

    odd_count = 0
    for value in H.values():
        odd_count += value % 2  # If divisible by 2 returns 0 if not returns 1
        if odd_count > 1:
            return False

    return True


print(palindrome_permutation("taco cato"))
