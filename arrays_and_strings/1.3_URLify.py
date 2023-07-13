# This solution has a time complexity of O(n), where n i s the length of the string. 
# It is a O(n) time complexity because the function peforms a signle pass through the 
# string to replace the spaces

def urlify(s, n):
	list_s = list(s[:n])

	for i in range(n):
		if list_s[i] == " ":
			list_s[i] = "%20"

	return ''.join(list_s)
	
print(urlify("Mr John Smith     ", 13))

		
