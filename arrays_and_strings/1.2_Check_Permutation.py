# The overall time complexity is O(n log n) for sorting the strings. Plus O(n) for the comparison. The 
# result time-complexity is O(n log n) because O(n log n) dominates the O(n) term.

def check_permutation_sorted(s1, s2):
	if len(s1) != len(s2):
		return False
	sorted_s1 = sorted(s1)
	sorted_s2 = sorted(s2)
	
	for i in range(len(s1)):
		if sorted_s1[i] != sorted_s2[i]:
			return False
			
	return True


s1 = "taco cat"
s2 = "cat taco"

print("Check Permutation Sorted", check_permutation_sorted(s1, s2))

# This solution has a time complexity of O(n). The implementation of the hashmap allows us to keep count 
# of all the characters in the string. We iterate through both strings which takes O(n) time. 

def check_permutation_hashmap(s1, s2):
	if len(s1) != len(s2):
		return False
		
	H = dict()
	
	for i in s1:
		if i in H:
			H[i] += 1
		else: 
			H[i] = 1
		
	for j in s2: 
		if j in H: 
			H[j] -= 1
		else: 
			return False 
		
	return all(value == 0 for value in H.values()) # returns True if all items in an iterable are true, otherwise it returns False
	
print("Check Permutation Hashmap", check_permutation_hashmap(s1, s2))
	
	
