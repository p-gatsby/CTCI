# This solution uses a hashmap and the time complexity is O(n), where n is the length of the string `s`.
# The space complexity is also O(n), where n is the number of unique characters in the string, 
# because in the worst-case scenario (when all characters are unique), the size of the dictionary 
# grows linearly with the size of the input string.

def is_unique_hashmap(s):
    H = dict()
    for i in s:
        if i in H:
            return False
        else: 
            H[i] = 1

    return True

print("Hashmap", is_unique_hashmap('Hello'))
print("Hashmap", is_unique_hashmap('Taco'))

# Without the use of additional data structures and alternative solution is to use two nested 
# for loops to compare each pair of characters. This would result in a time complexity of O(n^2).

def is_unique_nested_loops(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                return False
    
    return True

print("Nested Loops", is_unique_nested_loops('Hello'))
print("Nested Loops", is_unique_nested_loops('Taco'))

# A solution that is O(n log n) can be accomplished by sorting the string first.
def is_unique_sorted_loop(s):
    sorted_s = sorted(s)

    for i in range(1, len(sorted_s)):
        if sorted_s[i] == sorted_s[i-1]:
            return False
        
    return True

print("Sorted Loops", is_unique_sorted_loop('Hello'))
print("Sorted Loops", is_unique_sorted_loop('Taco'))

# Another solution that is O(n) can be solved by using a boolean array of size 128 for each possible
# ASCII character to keep track of seen characters. 

def is_unique_ascii(s):
    if len(s) > 128:  # More characters than possible in ASCII, so must be a duplicate
        return False
    
    seen_chars = [False] * 128
    for char in s:
        ascii_val = ord(char)
        if seen_chars[ascii_val]:  # Already seen this character
            return False
        seen_chars[ascii_val] = True  # Mark as seen
    
    return True

print("ASCII function", is_unique_ascii('Hello'))
print("ASCII function", is_unique_ascii('Taco'))
