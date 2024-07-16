def groupAnagrams(strs):
    anagrams = {}
    
    for s in strs:
        key = ''.join(sorted(s))
        
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    
    return list(anagrams.values())

# Example:
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = groupAnagrams(input_list)
print(output) 
