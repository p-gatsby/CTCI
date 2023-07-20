# Runtime complexity is O(n), where n is the length of the string. While inside the loop, each
# operation takes constant time O(1)

def string_compression(s):
    current_char = s[0]
    count = 1
    i = 1
    compressed_s = ""
    while i < len(s) and len(s) > len(compressed_s):
        if current_char == s[i]:
            count += 1
        else:
            compressed_s += f"{current_char}{count}"
            current_char = s[i]
            count = 1
            
        
        i += 1

    compressed_s += f"{current_char}{count}"
    

    if len(s) < len(compressed_s):
        return s
    
    return compressed_s

print(string_compression("aabcccccaaa"))