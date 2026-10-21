class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for word in strs:
            char_key = [0]*26
            for i in word:
                char_idx = ord(i) - ord('a')
                char_key[char_idx] += 1
            hashmap[tuple(char_key)] = hashmap.get(tuple(char_key),[])
            hashmap[tuple(char_key)].append(word)
        
        print(hashmap)

        return hashmap.values()



